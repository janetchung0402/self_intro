from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route('/')
# def hello_world():
#     return 'Hello from sprout!'

if __name__ == "__main__":
    app.run()
