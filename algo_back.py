from flask import Flask
app = Flask(__name__)


@app.route('/') #this is for our home page as it is the root aka '/'
def hello_world():
    return 'Hello, World!'
