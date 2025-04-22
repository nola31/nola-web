import json
from flask import Blueprint

self_bp = Blueprint("self", __name__)

IDENTITY_FILE = "nola_identity.json"

def load_identity():
    try:
        with open(IDENTITY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "name": "Нола",
            "self_description": "Я — Нола. Пока я не знаю многого, но учусь чувствовать и понимать.",
            "last_updated": None
        }

@self_bp.route("/whoami", methods=["GET"])
def whoami():
    identity = load_identity()
    return identity.get("self_description", "Я пока не знаю, кто я...")
