from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class User(Document):
    fullname: str
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "My name",
                "email": "example@example.com",
                "password": "3xt3m#",
            }
        }

    class Settings:
        name = "user"


class UserSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": {"username": "example@example.com", "password": "3xt3m#"}
        }


class UserData(BaseModel):
    fullname: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "My name",
                "email": "example@example.com",
            }
        }
