If you mean the app instance created by:
from fastapi import FastAPI

```python
app = FastAPI()
```

then app is a FastAPI object (which extends Starlette). Here are the most commonly used methods and attributes.
HTTP Route Decorators
```python
app.get(path)
app.post(path)
app.put(path)
app.delete(path)
app.patch(path)
app.options(path)
app.head(path)
app.trace(path)

Example:
@app.get("/users")
def get_users():
    return []
```

Generic Route Registration
app.api_route(path, methods=[...])

Example:
```python
@app.api_route("/items", methods=["GET", "POST"])
async def items():
    ...
```

Add Routes Programmatically
```python
app.add_api_route()
app.add_route()
app.mount()
app.include_router()
app.websocket()
app.add_websocket_route()
```
Example:
```python
app.include_router(router, prefix="/api")

app.mount("/static", StaticFiles(directory="static"))

app.add_api_route(
    "/hello",
    hello_function,
    methods=["GET"]
)
```

Middleware
```python
app.middleware("http")
app.add_middleware()
```
Example:
```python
@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)
    return response
```

Exception Handling
```python
app.exception_handler()
app.add_exception_handler()
```

Example:
```python
@app.exception_handler(ValueError)
async def handler(request, exc):
    ...
```

Event Handlers
Older style:
```python
@app.on_event("startup")
@app.on_event("shutdown")
```
Preferred newer style:
```python
FastAPI(lifespan=lifespan)
```

OpenAPI / Documentation
```python
app.openapi()
app.openapi_schema
app.openapi_url
app.docs_url
app.redoc_url
app.swagger_ui_html()
app.swagger_ui_oauth2_redirect_html()
```

URL Utilities
```python
app.url_path_for()
```
Example:
```python
url = app.url_path_for("get_user", id=1)
```

State
app.state

Example:
app.state.db = database

Access later:
request.app.state.db


Dependency Overrides
app.dependency_overrides

Example:
app.dependency_overrides[get_db] = fake_db


Lifespan / Startup
app.router.lifespan_context

Usually configured via:
```python
app = FastAPI(lifespan=my_lifespan)


Properties
app.routes
app.router
app.user_middleware
app.exception_handlers
app.state
app.debug
app.title
app.version
app.description
app.contact
app.license_info
app.openapi_tags
app.servers


Constructor Options (FastAPI(...))
app = FastAPI(
    title="My API",
    version="1.0.0",
    description="Demo",
    debug=True,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    openapi_tags=[...],
    lifespan=my_lifespan,
    dependencies=[...],
    middleware=[...],
)


Special Decorators
@app.get()
@app.post()
@app.put()
@app.delete()
@app.patch()
@app.options()
@app.head()
@app.trace()
@app.websocket()
@app.middleware()
@app.exception_handler()
@app.on_event()
```

Inspect Everything Available
To see every public method and attribute on your installed FastAPI version:
from fastapi import FastAPI

app = FastAPI()

print([name for name in dir(app) if not name.startswith("_")])

Or inspect callable methods only:
import inspect

for name, member in inspect.getmembers(app):
    if callable(member) and not name.startswith("_"):
        print(name)

This will list all methods available in the specific FastAPI version you have installed.



—------------------------------------------------------------------------------------------------

@app.get(
    path,
    *,
    response_model=None,
    status_code=200,
    tags=None,
    summary=None,
    description=None,
    response_description="Successful Response",
    deprecated=False,
    operation_id=None,
    responses=None,
    name=None,
    dependencies=None,
    response_class=JSONResponse,
    callbacks=None,
    openapi_extra=None,
    include_in_schema=True
)

—--------------------------------------------------------------------------------------------------------

from fastapi import Request

@app.exception_handler(ValueError)
async def value_error(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "message": str(exc)
        }
    )
—-----------------------------------------------------------------------------------
@app.middleware("http")
async def log(request, call_next):
    print("Before")

    response = await call_next(request)

    print("After")

    return response

—-------------------------------------------------------------------------------------------------

@app.on_event("startup")

@app.on_event("shutdown")
—--------------------------------------------------

@app.on_event("startup")
async def startup():
    print("Connecting database")

@app.on_event("shutdown")
async def shutdown():
    print("Closing database")

—-----------------------------------------------------------------------------------------------
The decorators @app.get(), @app.post(), @app.put(), @app.delete(), @app.patch(), @app.options(), @app.head(), and @app.trace() all accept many of the same optional parameters:

|Parameter|Purpose|
|---------|-------|
|path     |URL path (required)|
|response_model|Validate and shape the response|
|status_code|Default HTTP status code|
|tags|Group endpoints in Swagger UI|
|summary|Short description in OpenAPI|
|description|Detailed endpoint description|
|response_description|Description of the response in OpenAPI|
|deprecated|Mark endpoint as deprecated|
|operation_id|Custom OpenAPI operation ID|
|responses|Document additional response codes|
|name|Internal route name for URL generation|
|dependencies|Dependencies to execute for the route|
|response_class|Response type (e.g., JSON, HTML, PlainText)|
|callbacks|OpenAPI callback definitions|
|openapi_extra|Extra OpenAPI metadata|
|include_in_schema|Whether to include the route in generated API docs|



