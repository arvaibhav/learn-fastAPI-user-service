from src.db.tortoise_connection import init
from src.db.models.user import User
from src.utils.string_hasher import hash_string
import asyncio


# Create an async function to run your code
async def main():
    # Initialize the ORM connection
    await init()

    # Assuming you have a function that hashes the password before storing it.
    hashed_password = hash_string("yourpassword")

    # Create the user
    try:
        await User.create(
            username="ABC23", password_hash=hashed_password, email="abc@example.com"
        )
        print("User created successfully.")
    except Exception as e:
        print(f"Error creating user: {str(e)}")


if __name__ == "__main__":
    # Create an asyncio event loop
    loop = asyncio.get_event_loop()

    # Run the main function within the event loop
    loop.run_until_complete(main())
