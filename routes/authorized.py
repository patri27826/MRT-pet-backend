from fastapi import APIRouter, Depends

from auth.jwt_bearer import JWTBearer

router = APIRouter(dependencies=[Depends(JWTBearer())])


@router.post("/")
async def token_verify():
    return
