from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/demo",
    tags=["demo"],
)


@router.get("/", tags=[""], response_description="Returns a list of countries")
async def read(request: Request):
    try:
        return {"message": "demo processed."}
    except:
        return {"message": "There was an error"}
