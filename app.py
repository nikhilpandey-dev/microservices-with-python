from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello from flask in realworld and not a docker container, which I've removed!"
