from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr, Field
from src.core.user_auth import UserJWTAuthToken, create_jwt_token_for_user
from src.dao.user import get_user_by_username
from src.db.models.user import User_Pydantic, User
from src.utils.string_hasher import hash_string

router = APIRouter()


class UserProfile(BaseModel):
    user: User_Pydantic
    auth: UserJWTAuthToken


class UserAuthRequest(BaseModel):
    username: type(User.username)
    password: constr(max_length=48) = Field(
        ...,
        description="The user's password. Must be no more than 48 characters.",
        min_length=8,
    )


class UserSignupSchema(BaseModel):
    username: type(User.username)
    email: type(User.email)


@router.post("/login", response_model=UserProfile)
async def user_login(user_auth: UserAuthRequest):
    user = await get_user_by_username(user_auth.username)
    if not user:
        raise HTTPException(status_code=401, detail="username not found")
    if not user.is_valid_password(user_auth.password):
        raise HTTPException(status_code=401, detail="invalid password")

    user_auth = await create_jwt_token_for_user(user.username)
    return UserProfile(auth=user_auth, user=user)


@router.post("/signup", response_model=UserJWTAuthToken)
async def user_signup(user_auth: UserAuthRequest, user: UserSignupSchema):
    if await get_user_by_username(user_auth.username):
        raise HTTPException(
            status_code=401, detail="account with this username already created"
        )
    user = await User.create(
        username=user.username,
        password_hash=hash_string(user.password),
        email=user.email,
    )

    user_auth = await create_jwt_token_for_user(user.username)
    return user_auth
