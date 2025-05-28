from model.user import User

import requests
from flask import request
from peewee import JOIN
from werkzeug.security import generate_password_hash, check_password_hash

class Repository:
    @staticmethod
    def auth(username, password):
        user = User.get_user_by_name(username)
        if user is None:
            return {"user": user, "success": False}
        if check_password_hash(user.password, password):
            return {"user": user, "success": True}
        else:
            return {"user": user, "success": False}

    @staticmethod
    def register():
        username = request.form.get("uname")
        password = generate_password_hash(request.form.get("psw"))
        nickname = request.form.get("nickname")
        avatar = request.form.get("avatar")
        admin = "admin" in request.form
        user = User.create_user(username, password, nickname, avatar, admin)
        return user

    @staticmethod
    def get_user_by_id(userid):
        return User.get_user_by_id(userid)