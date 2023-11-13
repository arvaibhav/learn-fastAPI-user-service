from tortoise import Model, fields


class UserAuth(Model):
    token_id = fields.BigIntField(pk=True)
    user = fields.ForeignKeyField("models.User", null=True, on_delete=fields.CASCADE)
    is_evoked = fields.BooleanField(default=False)
    expires_in_sec = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
