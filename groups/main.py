from fastapi import FastAPI
from .router import router

app = FastAPI(title="Groups")


@app.get('/')
def groups_home():
    return {"message": "Groups"}


app.include_router(router)
