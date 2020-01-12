from flask import Flask,render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import SignupForm, SigninForm

main = Flask(__name__)
main.config['SECRET_KEY'] = '35c918c62246'
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///site.db'

db = SQLAlchemy(main) 

class User(db.Model):
    id = db.column(db.Interger, primary_key=True)
    username = db.column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(15), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.model):
    id = db.Column(db.Interger, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', )"

egs = [
    {'one' : 'baby',
    'two': 'mother',
    'three': 'father'},

    {'one' : 'babies',
    'two': 'mothers',
    'three': 'fathers'}
]

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Project Pitch', egs=egs)

@main.route('/signup', methods=['GET', 'POST'])
def Signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created succesfully for {form.username.data}!', 'success')
        return redirect(url_for('index'))

    return render_template('sign_up.html', title='Sign Up', form=form)

@main.route('/signin', methods=['GET', 'POST'])
def Signin():
    form = SigninForm()
    if form.validate_on_submit():
        if form.email.data == 'murathe@gmail.com' and form.password.data == 'murathe':
            flash(f'Succesfully logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Wrong credentials entered, please retry.', 'danger')
    return render_template('sign_in.html', title='Sign In', form=form)

@main.route('/interview')
def Interview():
    return render_template('interview.html', title='Sign In')

@main.route('/leadership.html')
def Leadership():
    return render_template('leadership.html', title='Sign In')

@main.route('/product')
def Product():
    return render_template('product.html', title='Product')


if __name__ == "__main__":
    main.run(debug=True)