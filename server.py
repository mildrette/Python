# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, I am learning Python for Backend"

# app.run(port=5000)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am learning Python for Backend"

app.run(port=5000)