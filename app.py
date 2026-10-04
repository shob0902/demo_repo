"""Toy Flask signup API -- the end-to-end demo target for the agent swarm.

Deliberately small: the Coder agent rewrites whole files, so everything here
stays well under the output-token ceiling documented in the main README.
"""
from flask import Flask, jsonify, request

from validators import is_valid_email

app = Flask(__name__)

users = []


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True, silent=True) or {}
    email = data.get("email", "")
    password = data.get("password", "")

    if not password:
        return jsonify({"error": "Password is required"}), 400
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email address"}), 400

    users.append({"email": email, "password": password})
    return jsonify({"status": "ok", "email": email}), 201


@app.route("/users", methods=["GET"])
def list_users():
    return jsonify({"users": [u["email"] for u in users]}), 200


@app.errorhandler(404)
def handle_404(error):
    return (
        jsonify({
            "error": "Not Found",
            "message": "The requested URL was not found on the server."
        }),
        404,
    )


if __name__ == "__main__":
    app.run(debug=True)
