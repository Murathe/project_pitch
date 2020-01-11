from flask import Flask,render_template
main = Flask(__name__)

@main.route('/')
@main.route('/index')
def Index:
    return render_template('index.html')

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