from fastapi import FastAPI

from app.api.routers import users
from app.core.logging import logger

app = FastAPI(title="TaskFlow API")
app.include_router(users.router)


@app.get("/logs/")
def read_root():
    logger.debug("Debug message from logs endpoint")
    logger.info("Info message from logs endpoint")
    return {"message": "Hello from logs endpoint"}
