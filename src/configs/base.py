import pydantic


class JWTConfig(pydantic.BaseSettings):
    token_expires_in: int = 60 * 60  # default 1 hour
    refresh_token_expires_in: int = 60 * 60 * 24 * 7  # default: 7 days

    class Config:
        env_prefix = 'JWT_'


class BaseConfig(pydantic.BaseSettings):
    jwt_config: JWTConfig = JWTConfig()

    class Config:
        env_file = '.env'
