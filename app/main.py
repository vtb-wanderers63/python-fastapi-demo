from fastapi import FastAPI
from app.routes.v1 import demov1
from app.routes.v1 import healthv1

app = FastAPI()

app.include_router(demov1)
app.include_router(healthv1)