from flask import Flask, json, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")

# def index():
#     return "index"

def index():
    return jsonify({
        "data": data,
        "message": "success"
    }, 200)

@app.route("/planet")

def getData():
    name = request.args.get("name")
    planetData = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planetData,
        "message": "success"
    })

if __name__ == "__main__":
    app.run()

