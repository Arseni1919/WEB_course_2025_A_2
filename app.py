import time

from flask import Flask
from flask import redirect, url_for
from flask import render_template
from flask import request
from flask import session
import json


app = Flask(__name__)
app.secret_key = '123'


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

#############################

@app.route('/contacts')
def contacts_func():
    if session['logged_in']:
        pass
        username = session['username']
        # DB
        contacts = ['Yossi', 'Ariel', 'Roberto']
        return render_template('contacts.html', contacts=contacts)
    message = 'Please register first!'
    return render_template('contacts.html', message=message)



@app.route('/block_example')
def block_example_func():
    return render_template('block_example.html')


@app.route('/get_post_example', methods=['GET', 'POST'])
def get_post_example_func():
    request_method = request.method
    if request_method == 'GET':
        # GET method
        if 'first_name' in request.args:
            first_name = request.args['first_name']
            last_name = request.args['last_name']
            # check DB
            return render_template(
                'get_post_example.html',
                request_method=request_method,
                first_name=first_name,
                last_name=last_name
            )
        return render_template(
            'get_post_example.html',
            request_method=request_method
        )
    else:
        # POST method
        username = request.form['username']
        password = request.form['password']
        # check DB
        # return redirect('/')
        return render_template(
            'get_post_example.html',
            request_method=request_method,
            username=username,
            password=password
        )

@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    # check DB
    session['username'] = username
    session['logged_in'] = True
    return redirect('/')


@app.route('/logout')
def logout_func():
    session['username'] = None
    session['logged_in'] = False
    return redirect('/')



# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# FETCH
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #

@app.route('/fetch_page')
def fetch_page_func():
    return render_template('fetch_example.html')


@app.route('/fetch_example', methods=['GET', 'POST'])
def fetch_example_func():
    if request.method == 'GET':
        data = {'message': 'This message is from /fetch_example route!'}
        time.sleep(1)
        return json.dumps(data)
    elif request.method == 'POST':
        data = request.json
        # check DB
        res = {'message': 'success'}
        return json.dumps(res)
    else:
        raise RuntimeError()










# @app.route('/fetch_example', methods=['GET', 'POST'])
# def fetch_example_func():
#     if request.method == 'GET':
#         data = {'message': 'GET response'}
#         return json.dumps(data)
#     if request.method == 'POST':
#         mydict = request.json
#         print(type(mydict))
#         print(mydict)
#         data = {'message': 'POST response'}
#         data.update(mydict)
#         return json.dumps(data)
#     raise RuntimeError('no no')
