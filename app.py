# app.py

from flask import Flask, jsonify, request
from user import greeting, goodbye, age
from working import print_board, solve, valid, find_empty

# import data

app = Flask(__name__)


@app.route("/")
def hello():
    return f"Hello World"


@app.route("/test")
def test():
    return jsonify({"message": "hello world"})


@app.route("/users")
def users():
    greeting()
    goodbye()
    print(age)
    return jsonify({"username": "john", "email": "john@john.com"})


@app.route("/public")
def public():
    return jsonify(
        {"id": 123, "locked": False, "name": "John", "roles": ["admin", "employee"]}
    )


@app.route("/sudoku", methods=["GET", "POST"])
def sudoku():
    data = request.get_json()
    print(data)
    # return "Welcome to Sudoku, Bye!"
    board = data["board"]
    result = solve(board)
    return jsonify({"board": result})


@app.route("/json", methods=["GET", "POST"])
def json_example():

    req = request.get_json()
    print(req)
    # return "Thanks!", 200

    return jsonify({"name": "Julian", "message": "Posting JSON data to Flask!"})


if __name__ == "__main__":
    app.run(debug=True)
