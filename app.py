from flask import Flask
from flask import redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/index')
@app.route('/home')
@app.route('/')
def home_page():
    # import data from DB
    # first_name = ''
    # last_name = 'Felner'
    # age = 100
    user = {
        'first_name': 'Ariel',
        'last_name': 'Felner',
        'age': 50
    }
    # user = None
    hobbies = ['Prog.', 'Running', 'Painting']
    degrees = ('B.Sc.', 'M.Sc.')
    return render_template(
        'index.html',
        user=user,
        hobbies=hobbies,
        degrees=degrees
    )

@app.route('/customer', methods=['GET'])
def customer_func():
    # data processing
    return redirect(url_for('home_page'))


@app.route('/customers')
def customers_page():
    return 'Welcome to Customers Page!!!!!'


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/customer/5/cart')
def customer_5_func():
    return 'Customer 5 - Cart'


