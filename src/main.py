from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.router import base_router
from api.common.middlewares import logging_middleware
from db.tortoise_connection import init, close_connections

app = FastAPI()

# app startup event
app.add_event_handler("startup", init)

# app shutdown event
app.add_event_handler("shutdown", close_connections)

# Middlewares
# 1.CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
)
# 2.File Logging
# app.middleware('http')(logging_middleware)

# Base Router
app.include_router(base_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
