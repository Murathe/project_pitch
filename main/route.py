from flask import render_template, url_for, flash, redirect
from main import main, db, bcrypt
from main.forms import SigninForm, SignupForm
from main.models import User, Post


egs = [
    {'title' : 'baby',
    'author': 'mother',
    'content': 'father'},

    {'title' : 'baby',
    'author': 'mother',
    'content': 'father'}
]

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Project Pitch', egs=egs)

@main.route('/signup', methods=['GET', 'POST'])
def Signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.add(user)
        db.session.commit()
        flash(f'Account created succesfully, log in to continue!', 'success')
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

@main.route('/profile')
def Profile():
    return render_template('profile.html', title='Profile')

@main.route('/interview')
def Interview():
    return render_template('interview.html', title='Sign In')

@main.route('/leadership.html')
def Leadership():
    return render_template('leadership.html', title='Sign In')

@main.route('/product')
def Product():
    return render_template('product.html', title='Product')