from fastapi import APIRouter, Request

router = APIRouter(
    # prefix="/",
    tags=["health"],
)


@router.get("/", tags=[""], response_description="Returns health status")
async def read(request: Request):
    try:
        return {"message": "App is running."}
    except:
        return {"message": "App is running but endpoint is failing"}


@router.get("/health", tags=[""], response_description="Returns health status")
async def read(request: Request):
    try:
        return {"message": "App is running."}
    except:
        return {"message": "App is running but endpoint is failing"}
