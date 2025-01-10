from fastapi import FastAPI
from routes.v1 import demov1

app = FastAPI()

app.include_router(demov1)
