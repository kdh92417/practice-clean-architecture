from peewee import *

# DB를 동적으로 처리하기위해 None으로 변경
db = SqliteDatabase(None)


class BaseModel(Model):
    class Meta:
        database = db


class UserModel(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = "users"
