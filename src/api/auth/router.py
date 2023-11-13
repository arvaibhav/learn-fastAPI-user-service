from fastapi import APIRouter, Body

from src.utils.jwt_auth import fetch_jwt_token

router = APIRouter()


@router.post("/token/refresh")
async def validate_refresh_token(
    username=Body(...), access_token=Body(...)
) -> dict[str, str]:
    token_payload = fetch_jwt_token(access_token)
    token_username = token_payload.username
    return {"status": "ok"}
