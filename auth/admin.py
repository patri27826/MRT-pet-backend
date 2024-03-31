from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

from database.database import user_collection

security = HTTPBasic()
hash_helper = CryptContext(schemes=["bcrypt"])


async def validate_login(credentials: HTTPBasicCredentials = Depends(security)):
    user = user_collection.find_one({"email": credentials.username})
    if user:
        password = hash_helper.verify(credentials.password, user["password"])
        if not password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
            )
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password"
    )
