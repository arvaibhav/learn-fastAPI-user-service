from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields
from src.utils.string_hasher import verify_hashed_string


class User(Model):
    username = fields.CharField(max_length=128, pk=True)
    password_hash = fields.CharField(max_length=128)
    email = fields.CharField(max_length=256)

    def is_valid_password(self, password):
        return verify_hashed_string(password, self.password_hash)


User_Pydantic = pydantic_model_creator(User, name="User")
