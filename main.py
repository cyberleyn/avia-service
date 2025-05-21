import json
import os

CONFIG_FILE = os.path.join("config", "config.json")
DEFAULT_CONFIG = {
    "admin_key": "admin",
}

if not os.path.exists(CONFIG_FILE):
    print("Конфиг отсутствует, добавлен конфиг по умолчанию")
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)
    print(f"Создан дефолтный конфиг: {CONFIG_FILE}")

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)
    ADMIN_KEY = config["admin_key"]
