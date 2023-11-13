from pydantic import BaseModel
from src.configs import APP_CONFIG
from src.db.models import UserAuth
from src.utils.jwt_auth import create_jwt_token


class AccessTokenPayload(BaseModel):
    username: str
    token_id: int = None


class RefreshTokenPayload(BaseModel):
    username: str
    token_id: int = None


class UserJWTAuthToken(BaseModel):
    token_type: str = "bearer"
    access_token: str
    refresh_token: str
    expires_in_sec: int
    refresh_expires_in: int


async def create_jwt_token_for_user(
        username: str, access_token_payload: AccessTokenPayload = None
) -> UserJWTAuthToken:
    if not access_token_payload:
        access_token_payload = AccessTokenPayload()

    user_auth_instance: UserAuth = await UserAuth.create(
        user_id=username,
        expires_in_sec=APP_CONFIG.jwt_config.token_expires_in,
    )
    token_id = user_auth_instance.token_id
    access_token_payload.token_id = token_id

    # Create JWT token with the `auth_payload`
    access_token = create_jwt_token(
        data=access_token_payload.model_dump(), expires_in=user_auth_instance.expires_in_sec
    )

    # Create JWT Refresh Token with reference of last access id
    refresh_token = create_jwt_token(
        data=RefreshTokenPayload(token_id=token_id, username=username).model_dump(),
        expires_in=APP_CONFIG.jwt_config.refresh_token_expires_in,
    )

    # Return the typical JWT view
    return UserJWTAuthToken(access_token=access_token, refresh_token=refresh_token)


def get_access_token_payload(access_token):
    pass


def get_refresh_token_payload(refresh_token):
    pass
