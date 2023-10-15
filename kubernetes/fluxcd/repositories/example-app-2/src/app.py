from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! hongphuc5497/example-app-2:0.0.2"
