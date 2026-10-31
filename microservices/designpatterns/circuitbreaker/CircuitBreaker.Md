# CircuitBreaker

## Circuit Breaker Pattern 
- The Circuit Breaker is a design pattern used in microservices to prevent an application from repeatedly calling a service that is failing or unavailable
- Circuit breaker temporarily stops requests to an unhealthy service, allowing it time to recover

- Imagine you have a FastAPI application that calls an external Payment API
- Without a circuit breaker, every incoming request may wait for the failing Payment API. This can consume connections, workers, and resources, potentially affecting your entire application
- With a circuit breaker, the application detects repeated failures and temporarily rejects calls without contacting the failing service

## The three circuit breaker states
- **CLOSED — Normal operation** : Requests are allowed to reach the external service. The circuit breaker monitors failures
- **OPEN — Service is failing**: After the failure threshold is reached, calls are blocked immediately for a configured period
- **HALF-OPEN — Recovery test**: After the waiting period, a limited number of test requests are allowed. Success closes the circuit; failure opens it again

## Python + FastAPI example

- **Scenario**: If the Payment Service fails 3 consecutive times, open the circuit for 10 seconds. After 10 seconds, allow one recovery request
- Step 1: Install FastAPI
```bash
pip install fastapi uvicorn
```
- Step 2: Create circuitbreaker.py

- Step 3: Run the application
```bash
uvicorn circuitbreaker:app --reload
```

## Test the circuit breaker

- Use the endpoints in Swagger UI in this order
- http://127.0.0.1:8000/docs
- Test 1 — Fail three times
	- Call POST /pay three times while the payment service is down
		- First two calls: 502 Bad Gateway. Third call: 502, and the circuit opens
- Test 2 — Call again immediately
	- Call POST /pay once more.
		- Response: 503 Service Unavailable. The payment function is not called.
- Test 3 — Wait 10 seconds
	- Call POST /pay again
		- The circuit moves to HALF-OPEN and permits one recovery test. Since the service is still down, the circuit reopens.
- Test 4 — Recover the payment service
	- Call POST /demo/payment-service?down=false, wait 10 seconds if the circuit is open, then call POST /pay.
		Response: 200 OK — {"message": "Payment successful"}. The circuit closes.
		

## 5. Circuit Breaker vs. Retry

| Feature  | Retry                             | Circuit Breaker                     |
| -------- | --------------------------------- | ----------------------------------- |
| Purpose  | Attempts a failed operation again | Stops calls to an unhealthy service |
| Behavior | Repeats requests                  | Blocks requests when open           |
| Best use | Temporary failures                | Persistent failures                 |
| Example  | Retry after a timeout             | Reject calls for 10 seconds         |

They can be used together, but retries should be limited; otherwise, they may increase the load on an already failing service.

## Notes:

- The Circuit Breaker pattern protects microservices from cascading failures. It has three states: CLOSED, OPEN, and HALF-OPEN. In the CLOSED state, requests flow normally while failures are monitored. When failures exceed a configured threshold, the circuit opens and rejects calls without invoking the downstream service. After a recovery timeout, it enters HALF-OPEN and allows a limited test request. If the request succeeds, the circuit closes; otherwise, it opens again. In Python and FastAPI, this pattern can protect calls to external REST APIs, payment gateways, databases, and other dependent services.

- **Important production note**: If you deploy FastAPI with multiple worker processes or multiple application instances, each instance of this in-memory breaker has its own state. Consider a mature circuit-breaker library or a distributed coordination approach when shared behavior is required


---
## Modules
- The two most prominent and production-ready packages for implementing this pattern in Python are pybreaker and circuitbreaker.

| Library | Key Advantages | Best Used For |
|---|---|---|
| pybreaker[](https://github.com/danielfm/pybreaker) | • Distributed state via Redis storage • Highly mature, stable, and battle-tested • Comprehensive event listeners | Multi-instance microservices, complex event monitoring, and web frameworks like Tornado. |
| circuitbreaker[](https://pypi.org/project/circuitbreaker/) | • Lightweight and intuitive API • Built-in fallback function arguments • Clean @circuit decorator syntax | Standard synchronous or asynchronous applications looking for a simple, low-boilerplate implementation. |
| purgatory[](https://github.com/mardiros/purgatory) | • Native asyncio optimization • Fully typed out-of-the-box | Modern asynchronous microservices and heavy asyncio pipelines. |


## Module :circuitbreaker : Example

### Installation:
```bash
pip install circuitbreaker
```

```python
import requests
from circuitbreaker import circuit

def handle_api_fallback():
    return {"status": "fallback", "data": "Service temporarily unavailable."}

# Automatically trips after 3 consecutive failures, stays open for 20 seconds
@circuit(failure_threshold=3, recovery_timeout=20, fallback_function=handle_api_fallback)
def fetch_external_data():
    response = requests.get("https://example.com", timeout=2.0)
    response.raise_for_statues()
    return response.json()
```
---


## Advanced module : pybreaker

### Installation:
```bash
pip install pybreaker

```

```python
import pybreaker
import requests

# Define the breaker configuration globally
db_breaker = pybreaker.CircuitBreaker(
    fail_max=5,                # Trip after 5 failures
    reset_timeout=30,          # Try again after 30 seconds
    exclude=[ValueError]       # Do not count client-side errors as failures
)

# Usage as a context manager
def query_database():
    try:
        with db_breaker:
            return requests.get("https://db-service/query")
    except pybreaker.CircuitBreakerError:
        # Executed instantly when circuit is OPEN without hitting the network
        return {"error": "Database service is offline"}

```

## FastAPI with circuitbreaker (Built-in Async Support)
```python
import httpx
from fastapi import FastAPI, HTTPException
from circuitbreaker import circuit

app = FastAPI()

# Fallback function must match the async nature of the route if it awaits anything
def api_fallback(*args, **kwargs):
    return {"status": "fallback", "message": "External API is down. Serving cached or generic data."}

# Circuit trips after 3 failures, stays OPEN for 15 seconds
@circuit(failure_threshold=3, recovery_timeout=15, fallback_function=api_fallback)
async def call_unreliable_service():
    async with httpx.AsyncClient() as client:
        # Intentionally low timeout to catch slow/hung dependencies
        response = await client.get("https://httpbin.org", timeout=2.0)
        return response.json()

@app.get("/data")
async def get_data():
    # If the circuit trips, this returns the fallback dictionary immediately
    data = await call_unreliable_service()
    return data
```

## FastAPI with pybreaker (Advanced/Context Manager)
```python
import httpx
import pybreaker
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Create a central circuit breaker instance
external_api_breaker = pybreaker.CircuitBreaker(
    fail_max=3,          # Trip after 3 failures
    reset_timeout=20     # Stay open for 20 seconds before attempting half-open
)

async def fetch_from_service():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://example.com", timeout=1.5)
        response.raise_for_status()
        return response.json()

@app.get("/external-status")
async def get_external_status():
    try:
        # Wrap your network/I/O operation inside the breaker context
        with external_api_breaker:
            data = await fetch_from_service()
            return {"status": "success", "data": data}
            
    except pybreaker.CircuitBreakerError:
        # Fast-fail: Triggered instantly when the circuit is OPEN 
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="The external service is currently offline. Please try again later."
        )
        
    except httpx.HTTPStatusError as exc:
        # Handle actual HTTP errors from the service
        raise HTTPException(status_code=exc.response.status_code, detail="Remote error")
```
## Modern Async Alternative (purgatory)
- If your entire stack is purely asynchronous, purgatory is purpose-built for FastAPI workflows and integrates smoothly with asynchronous dependency injection
```python
from fastapi import FastAPI, HTTPException, status
from purgatory import AsyncCircuitBreakerFactory

app = FastAPI()

# Initialize the factory (can be backed by Redis for multi-instance FastAPI)
circuit_breaker_factory = AsyncCircuitBreakerFactory()

@app.get("/purgatory-data")
async def get_purgatory_data():
    try:
        # Fetches or creates a breaker named 'external-service'
        async with await circuit_breaker_factory.get_breaker(
            "external-service", 
            threshold=3, 
            ttl=15
        ):
            async with httpx.AsyncClient() as client:
                res = await client.get("https://example.com")
                return res.json()
                
    except pybreaker.CircuitBreakerError: # Purgatory raises similar open state exceptions
        raise HTTPException(status_code=503, detail="Circuit Open")
```


