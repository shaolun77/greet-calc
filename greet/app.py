from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "welcome"

@app.route("/welcome/home")
def welcome_home():
    return "welcome home"

@app.route("/welcome/back")
def welcome_back():
    return "welcome back"

# In the greet folder, Make a simple Flask app that responds to these routes with simple text messages:

# /welcome
# Returns “welcome”
# /welcome/home
# Returns “welcome home”
# /welcome/back
# Return “welcome back”