from flask import Blueprint, request, jsonify
from services.auth_service import register_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    result = register_user(
        data["name"],
        data["email"],
        data["password"]
    )

    return jsonify(result)