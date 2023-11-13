from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["src.db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


# Initialize Tortoise with your configuration
async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    from src.db.models.user import User


# Close connections when your application shuts down
async def close_connections():
    await Tortoise.close_connections()
