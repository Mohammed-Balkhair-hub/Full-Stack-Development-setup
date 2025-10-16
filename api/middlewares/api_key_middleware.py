import os
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse


class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Skip API key check for the API documentation
        excluded_paths = ["/docs", "/redoc", "/openapi.json"]
        if request.url.path in excluded_paths:
            response = await call_next(request)
            return response
        authorization = request.headers.get("Authorization")
        if not authorization or not authorization.startswith("Bearer "):
            return JSONResponse(
                content={"error": "Invalid or missing authorization header"},
                status_code=401,
            )
        elif authorization.split("Bearer ")[1].strip() != os.getenv("API_SERVER_KEY"):
            return JSONResponse(
                content={"error": "Unauthorized. Invalid API key"},
                status_code=401,
            )
        response = await call_next(request)
        return response
