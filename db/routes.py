from flask import Blueprint

db = Blueprint("db", __name__)

@db.route("/hello")
def hello():
    return "Hello from db!"
