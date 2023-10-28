from fastapi import FastAPI
from .routers import users_router

app = FastAPI(title="Users")
app.include_router(users_router)