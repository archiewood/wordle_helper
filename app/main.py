from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
		return "<h1>Welcome to Wordle Helper!</h1>"
