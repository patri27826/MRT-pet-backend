from models.user import User

user_collection = User


async def add_user(new_user: User) -> User:
    user = await new_user.create()
    return user
