from .router import router
from fastapi import FastAPI

app = FastAPI(title="Groups")
app.include_router(router)
