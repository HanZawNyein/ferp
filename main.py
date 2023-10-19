from fastapi import FastAPI

from db import engine,Base

from core.config import settings
from apps import APPS

Base.metadata.create_all(bind=engine)

# apps
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# apps
for path, apps in APPS:
    app.mount(path, apps)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
