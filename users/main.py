from fastapi import FastAPI

from . import router

app = FastAPI(title="Users")

app.include_router(router.router)