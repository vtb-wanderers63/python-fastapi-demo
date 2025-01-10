from fastapi import FastAPI
from app.routes.v1 import demov1

app = FastAPI()

app.include_router(demov1)
