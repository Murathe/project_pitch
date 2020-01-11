from flask import Flask,render_template, url_for
from forms import Signup_form, Signin_form
main = Flask(__name__)

main.config['SECRET_KEY'] = '35c918c62246'

eg = [
    {'one' : 'baby'}
    {'two': 'mother'}
    {'three': 'father'}
]


@main.route('/')
@main.route('/index')
def Index:
    return render_template('index.html', eg=eg)

@main.route('/signup')
def Signup:

    form = Signup_form()

    return render_template('sign_up', title='Sign Up', form=form)

@main.route('/signin')
def Signup:

    form = Signup_form()

    return render_template('sign_up', title='Sign Up', form=form)

@main.route('/interview')
def Interview:
    return render_template('interview.html')

@main.route('/leadership.html')
def Leadership:
    return render_template('leadership.html')

@main.route('/product')
def Product:
    return render_template('product.html')


if __name__ == "__main__":
    main.run(debug=True)