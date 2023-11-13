from fastapi import Header

from src.utils.jwt_auth import fetch_jwt_token
from fastapi import Request, HTTPException


def get_auth_token_payload(token: str = Header(alias="Authorization")):
    try:
        token_payload = fetch_jwt_token(token=token.split(" ")[-1])
        return token_payload
    except:
        raise HTTPException(status_code=401, detail=["wrong token"])
