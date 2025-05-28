import json
import os
from pathlib import Path

from flask import *
from peewee import PostgresqlDatabase

from database import init_db
from repository import Repository


app = Flask(__name__)


@app.route("/", methods=['post', 'get'])
def index():
    if request.method == "GET":
        if not request.cookies.get("user"):
            return redirect(url_for("login"))
        else:
            userid = request.cookies.get("user")
            return redirect(url_for("dashboard"))


@app.route("/login", methods=['post', 'get'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("psw")
        auth = Repository.auth(username, password)
        if auth["success"]:
            userid = auth["user"].id
            response = make_response(redirect(url_for("dashboard")))
            response.set_cookie('user', str(userid))
            return response
        else:
            return render_template("login.html", error=True)


@app.route("/register", methods=['post', 'get'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        user = Repository.register()
        response = make_response(redirect(url_for("dashboard")))
        response.set_cookie("user", str(user.id))
        return response


@app.route("/dashboard", methods=['post', 'get'])
def dashboard():
    return render_template("dashboard.html")

@app.route("/profile/logout", methods=['GET', 'POST'])
def logout():
    response = make_response(redirect(url_for("index")))
    response.set_cookie('user', "", max_age=0)
    return response


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
