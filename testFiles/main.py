# main.py

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Call C function for user verification
    result = subprocess.run(["./program"], capture_output=True, text=True)
    if "success" in result.stdout:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401


@app.route("/api/signup", methods=["POST"])
def signup():
    return jsonify({"message": "Signup successful"}), 200


if __name__ == "__main__":
    app.run(debug=True)
