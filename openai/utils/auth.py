import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

USER_FILE = "users.json"

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(username, password, role="Elder User"):
    users = load_users()
    if username in users:
        return False
    users[username] = {
        "password": generate_password_hash(password),
        "role": role
    }
    save_users(users)
    return True

def authenticate(username, password):
    users = load_users()
    if username in users and check_password_hash(users[username]["password"], password):
        return True
    return False