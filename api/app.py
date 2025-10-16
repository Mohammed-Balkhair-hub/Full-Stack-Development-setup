import os
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from middlewares.api_key_middleware import APIKeyMiddleware


app = FastAPI(
    title="AI_LAB API",
    description="This is the documentation of the AI_LAB API.",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True},
)


security = HTTPBearer()

# CORS
origins = [
    "http://localhost",
    "http://localhost:" + os.getenv("REACT_APP_PORT"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(APIKeyMiddleware)

app.include_router(router, dependencies=[Depends(security)])


@app.exception_handler(404)
async def not_found(request, exc):
    return JSONResponse(
        content={"error": f"Resource not found: {request.url}"}, status_code=404
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("API_SERVER_PORT", 4000))
