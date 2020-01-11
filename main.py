from flask import Flask
main = Flask(__name__)

@main.route('/')
@main.route('/index')
def Index:
    