from flask import Flask,render_template, url_for, flash, redirect
from forms import SignupForm, SigninForm
main = Flask(__name__)

main.config['SECRET_KEY'] = '35c918c62246'

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

@main.route('/signup')
def Signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created succesfully for {form.username.data}.', 'success')
         

    return render_template('sign_up.html', title='Sign Up', form=form)

@main.route('/signin')
def Signin():
    form = SigninForm()

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