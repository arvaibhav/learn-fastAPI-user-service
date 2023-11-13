from fastapi import APIRouter, Depends
from .auth.router import router as auth_router
from .common.http_headers import user_common_headers
from .user.router import router as user_router

base_router = APIRouter(dependencies=[Depends(user_common_headers)])
base_router.include_router(router=auth_router, prefix="/auth", tags=["auth"])
base_router.include_router(router=user_router, prefix="/user", tags=["user"])
