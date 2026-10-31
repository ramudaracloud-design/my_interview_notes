# Custom FastAPI Middleware or Dependency to automatically apply circuit breaking to global routes
- Using a **FastAPI Dependency** is the cleanest, most idiomatic way to apply a global circuit breaker.
- While **Middleware** can intercept requests, it executes too early in the FastAPI lifecycle—before routing happens. 
- A global Dependency allows you to safely wrap your endpoints, access path details, and automatically catch circuit errors to return clean HTTP responses.

- Here is the production-ready implementation using pybreaker integrated as a global FastAPI dependency

### Step 1: Create the Dependency Boilerplate
- This module initializes your circuit breaker and creates a dependency callable that monitors route execution
```python
# dependencies.py
import pybreaker
from fastapi import HTTPException, status, Request

# 1. Initialize a global circuit breaker
# In production, you can swap this with a Redis storage backend
global_breaker = pybreaker.CircuitBreaker(
    fail_max=5,          # Open circuit after 5 failures
    reset_timeout=30     # Stay open for 30 seconds
)

# 2. Define the Dependency
async def global_circuit_breaker(request: Request):
    """
    FastAPI dependency that wraps route handling inside a circuit breaker.
    If the circuit opens, it fast-fails before executing the route logic.
    """
    try:
        # Enter the circuit breaker context
        # This will instantly raise CircuitBreakerError if the circuit is currently OPEN
        with global_breaker:
            # Yield control back to the route operation
            yield
            
    except pybreaker.CircuitBreakerError:
        # Prevent cascading failures by returning a 503 instantly
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "error": "Service Temporarily Unavailable",
                "message": "The system is experiencing high failure rates. Circuit breaker is open.",
                "path": request.url.path
            }
        )

```

## Step 2: Register it Globally in your App

- Apply the dependency to your entire FastAPI instance by passing it to the dependencies list during initialization.

```python
# main.py
import httpx
from fastapi import FastAPI, Depends
from dependencies import global_circuit_breaker

# Register the circuit breaker globally across ALL routes
app = FastAPI(dependencies=[Depends(global_circuit_breaker)])

@app.get("/unstable-data")
async def get_unstable_data():
    """
    This route automatically runs inside the circuit breaker.
    If 'httpbin' times out or errors out 5 consecutive times, 
    the entire endpoint blocks network traffic and triggers a 503.
    """
    async with httpx.AsyncClient() as client:
        # Simulating a slow endpoint that might trip our circuit
        response = await client.get("https://httpbin.org", timeout=1.0)
        return response.json()

@app.get("/health-check")
async def health():
    # Note: Because it's global, even this route is protected.
    # If the circuit trips due to /unstable-data failing, this will also return 503!
    return {"status": "healthy"}

```

## Excluding Specific Routes (Selective Application)

- Applying a circuit breaker globally means a failure on one route will trip the breaker for all routes (including health checks). 
- If you want to protect your core APIs but exclude /health or /metrics, remove it from the global FastAPI() definition and apply it to a APIRouter instead

```python
# main.py
from fastapi import FastAPI, Depends
from dependencies import global_circuit_breaker

app = FastAPI()

# 1. Public/Internal routes unaffected by the circuit breaker
@app.get("/health")
def health_check():
    return {"status": "alive"}

# 2. Protected routes bundled under an protected router
api_router = APIRouter(dependencies=[Depends(global_circuit_breaker)])

@api_router.get("/external-service-a")
async def service_a():
    return {"data": "A"}

@api_router.get("/external-service-b")
async def service_b():
    return {"data": "B"}

app.include_router(api_router, prefix="/api/v1")
```
