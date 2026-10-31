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
