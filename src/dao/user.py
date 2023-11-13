from typing import Union
from src.db.models import User
from tortoise.exceptions import DoesNotExist


async def get_user_by_username(username) -> Union[User, None]:
    try:
        return await User.get(username=username)
    except DoesNotExist:
        return None
