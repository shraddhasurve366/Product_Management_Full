from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Product Management API is running",
        "environment": settings.environment,
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
