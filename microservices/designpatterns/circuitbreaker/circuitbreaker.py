import asyncio
import time

from fastapi import FastAPI, HTTPException

app = FastAPI()

# Simulate an external payment service
PAYMENT_SERVICE_DOWN = True


class CircuitOpenError(Exception):
    pass


class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=10):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout

        self.state = "CLOSED"
        self.failures = 0
        self.opened_at = 0.0
        self.probe_in_progress = False
        self.lock = asyncio.Lock()

    async def call(self, func):
        async with self.lock:
            if self.state == "OPEN":
                if time.monotonic() - self.opened_at < self.recovery_timeout:
                    raise CircuitOpenError("Circuit is OPEN")

                self.state = "HALF_OPEN"

            if self.state == "HALF_OPEN":
                if self.probe_in_progress:
                    raise CircuitOpenError("Recovery test in progress")
                self.probe_in_progress = True

        try:
            result = await func()

        except Exception:
            async with self.lock:
                if self.state == "HALF_OPEN":
                    self.state = "OPEN"
                    self.opened_at = time.monotonic()
                    self.probe_in_progress = False
                else:
                    self.failures += 1

                    if self.failures >= self.failure_threshold:
                        self.state = "OPEN"
                        self.opened_at = time.monotonic()

            raise

        async with self.lock:
            self.state = "CLOSED"
            self.failures = 0
            self.probe_in_progress = False

        return result


breaker = CircuitBreaker()


async def payment_service():
    await asyncio.sleep(0.1)

    if PAYMENT_SERVICE_DOWN:
        raise RuntimeError("Payment Service unavailable")

    return {"message": "Payment successful"}


@app.post("/pay")
async def pay():
    try:
        return await breaker.call(payment_service)

    except CircuitOpenError as exc:
        raise HTTPException(status_code=503, detail=str(exc))

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Payment Service failed"
        )


@app.post("/demo/payment-service")
async def set_payment_service(down: bool):
    global PAYMENT_SERVICE_DOWN
    PAYMENT_SERVICE_DOWN = down
    return {"payment_service_down": down}


@app.get("/circuit-status")
async def circuit_status():
    return {
        "state": breaker.state,
        "failures": breaker.failures
    }
