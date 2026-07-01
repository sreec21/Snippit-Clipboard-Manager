from database.db import users
import bcrypt

def register_user(name, email, password):

    existing = users.find_one({"email": email})

    if existing:
        return {"message": "User already exists"}

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    users.insert_one({
        "name": name,
        "email": email,
        "password": hashed
    })

    return {"message": "User Registered Successfully"}