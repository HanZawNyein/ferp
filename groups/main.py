from fastapi import FastAPI
from .router import router

app = FastAPI(title="Groups")
app.include_router(router)
