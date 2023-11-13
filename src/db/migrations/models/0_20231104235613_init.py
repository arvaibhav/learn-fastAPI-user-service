from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "username" VARCHAR(128) NOT NULL  PRIMARY KEY,
    "password_hash" VARCHAR(128) NOT NULL,
    "email" VARCHAR(256) NOT NULL
);
CREATE TABLE IF NOT EXISTS "userauth" (
    "token_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "is_evoked" INT NOT NULL  DEFAULT 0,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" VARCHAR(128) REFERENCES "user" ("username") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
