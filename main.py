from fastapi import FastAPI,Response,Request

from db import engine,Base,SessionLocal

from core.config import settings
from apps import APPS


Base.metadata.create_all(bind=engine)

# apps
app = FastAPI(
    title=settings.PROJECT_NAME
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# apps
for path, apps in APPS:
    app.mount(path, apps)


@app.get("/")
async def root():
    return {"message": "Hello, FERP"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
