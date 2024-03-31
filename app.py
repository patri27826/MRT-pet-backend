from fastapi import Depends, FastAPI

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.authorized import router as UserAuthorizedRouter
from routes.user import router as UserRouter

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


app.include_router(UserRouter, tags=["User"], prefix="/users")
app.include_router(UserAuthorizedRouter, tags=["User"], prefix="/users")
