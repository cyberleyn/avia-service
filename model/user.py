from peewee import *

from database import pg_db

class User(Model):
    username = CharField()
    password = CharField()
    nickname = CharField()
    admin = BooleanField(default=False)
    avatar = CharField(default="https://cdn3.iconfinder.com/data/icons/avatars-15/64/_Ninja-2-1024.png")

    class Meta:
        database = pg_db

    @staticmethod
    def create_user(username, password, nickname, admin):
        user = User()
        user.username = username
        user.password = password
        user.nickname = nickname
        user.admin = admin
        user.save()
        return user

    @staticmethod
    def get_user_by_name(username):
        query = User.select().where(User.username == username)
        if query.exists():
            return query.get()

    @staticmethod
    def get_user_by_id(id):
        query = User.select().where(User.id == id)
        if query.exists():
            return query.get()

    @staticmethod
    def update_user(user, username=None, password=None, nickname=None, avatar=None, admin=None):
        if User.select().where(User.username == user.username, User.password == user.password, User.nickname == user.nickname,
                                 User.avatar == user.avatar).exists():
            updating_query = {}
            if username:
                updating_query['username'] = username
            if password:
                updating_query['password'] = password
            if nickname:
                updating_query['nickname'] = nickname
            if avatar:
                updating_query['avatar'] = avatar
            if admin:
                updating_query['admin'] = admin
            query = User.update(updating_query).where(User.username == user.username, User.password == user.password, User.nickname == user.nickname,
                                 User.avatar == user.avatar, User.admin == user.admin)
            query.execute()

