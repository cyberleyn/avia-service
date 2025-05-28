import json
import os
from pathlib import Path

from flask import *
from peewee import PostgresqlDatabase

DEFAULT_CONFIG = {
    "db_name": "my_db",
    "db_user": "user",
    "db_password": "3212",
    "db_host": "localhost",
    "db_port": 1221
}


def init_db():
    current_dir = Path(__file__).parent.resolve()
    CONFIG_FILE = current_dir / "config" / "config.json"
    if not os.path.exists(CONFIG_FILE):
        print("Конфиг отсутствует, добавлен конфиг по умолчанию")
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        print(f"Создан дефолтный конфиг: {CONFIG_FILE}")

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
        DB_NAME = config["db_name"]
        DB_USER = config["db_user"]
        DB_PASSWORD = config["db_password"]
        DB_HOST = config["db_host"]
        DB_PORT = config["db_port"]
    print(DB_NAME)
    pg_db = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    return pg_db


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
