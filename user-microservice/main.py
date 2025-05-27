import uvicorn
from fastapi import FastAPI
from routes.routes import api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=7000,
        log_level="info",
        reload=True
    )
    