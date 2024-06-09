from flask import Flask, request, jsonify

app = Flask(__name__)

username = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(username.keys()))


@app.route("/status")
def data():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = username.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    if new_user and "username" in new_user:
        username[new_user["username"]] = new_user
        return jsonify({"message": "User added successfully"}), 201
    else:
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run(debug=True)
