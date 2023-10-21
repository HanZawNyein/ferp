from fastapi import FastAPI, Response, Request

from ferp.db import engine, Base, SessionLocal

from ferp.core.config import settings
from ferp.apps import APPS

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
# app.include_router()
for path, apps in APPS:
    app.mount(path, apps)


@app.get("/")
async def root():
    return {"message": "Hello, FERP"}
