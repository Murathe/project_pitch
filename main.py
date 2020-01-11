from flask import Flask,render_template
main = Flask(__name__)

@main.route('/')
@main.route('/index')
def Index:
