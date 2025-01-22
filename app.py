# chrome://net-internals/#sockets
# chrome://net-internals/#sockets
# chrome://net-internals/#sockets
# chrome://net-internals/#sockets
# chrome://net-internals/#sockets
import time

from db_functions import customer_update

from flask import Flask
from flask import redirect, url_for
from flask import render_template
from flask import request
from flask import session
from flask import jsonify
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







# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# MONGODB
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://1919ars:1919ars@cluster0.kg52uoz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new cluster and connect to the server
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['mydatabase']
customers_col = mydatabase['customers']
products_col = mydatabase['products']

@app.route('/mongodb')
def mongodb_func():
    # message = 'good'
    # message = pymongo.version
    # message = cluster.list_database_names()
    # sample_analytics = cluster['sample_analytics']
    # message = sample_analytics.list_collection_names()

    # insert_one
    # my_dict = {
    #     'name': 'John',
    #     'address': 'Highway 37',
    #     'rating': 10
    # }
    # customers_col.insert_one(my_dict)
    # message = my_dict

    # insert_many
    # my_list = [
    #     {'name': 'Tal', 'address': 'Hogwards 37', 'rating': 11},
    #     {'name': 'Bekka', 'address': 'Bronx 3', 'rating': 20},
    #     {'name': 'Alisa', 'address': 'Area 9', 'rating': 30},
    # ]
    # customers_col.insert_many(my_list)
    # message = my_list

    # findOne
    # message = customers_col.find_one({'name': 'John'})

    # find
    # message = list(customers_col.find())

    # find query
    # myquery = {'name': 'John'}
    # myquery = {'rating': {"$gt": 10}}
    # message = list(customers_col.find(myquery))

    # sort
    # myquery = {'rating': {"$gt": 10}}
    # message = list(customers_col.find(myquery).sort('name'))
    # message = list(customers_col.find().sort('name', -1))
    # message = len(list(customers_col.find()))

    # limit
    # myquery = {'rating': {"$lt": 50}}
    # message = list(customers_col.find(myquery).sort('rating', -1).limit(3))
    # my_list = list(customers_col.find().sort('rating', -1).limit(3))

    # update one
    # my_query = {'address': 'Highway 37'}
    # new_values = {'$set': {'address': 'Canyon 123'}}
    # customers_col.update_one(my_query, new_values)
    # message = list(customers_col.find({'address': 'Canyon 123'}))

    # update many
    # customers_col.update_many({}, {'$inc': {'rating': 1}})
    # customers_col.update_many({}, {'$set': {'rating': 100}})
    # message = list(customers_col.find())

    # delete one
    # customers_col.delete_one({'name': 'Alisa'})
    # message = list(customers_col.find())

    # delete many
    # customers_col.delete_many({'rating': {'$gt': 1000}})
    # message = list(customers_col.find())

    # aggregations
    # aggregation = [
    #     {
    #         '$match': {
    #             'rating': 100
    #         }
    #     }, {
    #         '$sort': {
    #             'name': -1
    #         }
    #     }, {
    #         '$limit': 3
    #     }
    # ]
    # message = list(customers_col.aggregate(aggregation))

    message = ''
    my_list = list(customers_col.find())
    return render_template('mongodb_lecture.html', my_list=my_list)
    # return render_template('mongodb_lecture.html', message=message)


    # # return render_template('mongodb_lecture.html', message=message)
    # return render_template('mongodb_lecture.html', my_list=my_list)



@app.route('/db_insert')
def insert_func():
    # insert_one
    my_dict = {
        'name': request.args['name'],
        'address': request.args['address'],
        'rating': int(request.args['rating']),
    }
    customers_col.insert_one(my_dict)
    return redirect(url_for('mongodb_func'))



@app.route('/db_delete', methods=['POST'])
def delete_func():
    print(request.form)
    customers_col.delete_one({'name': request.form['name']})
    return redirect(url_for('mongodb_func'))



@app.route('/db_increment')
def increment_func():
    customers_col.update_many({}, {'$inc': {'rating': 1}})
    return redirect(url_for('mongodb_func'))



# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# REST API
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #



@app.route('/profiles', defaults={'user_id': 54321, 'category_name': 'DEFAULT CATEGORY'})
@app.route('/profiles/<int:user_id>/categories/<category_name>')
def profiles_func(user_id, category_name):
    # return render_template('profiles.html',
    #                        user_id=user_id, category_name=category_name
    #                        )
    data = {'user_id': user_id, 'category': category_name}
    return jsonify(data)
    # return json.dumps(data)

@app.route('/profiles/<int:user_id>/categories')
def profiles_categories_func(user_id):
    return render_template('profiles.html',
                           user_id=user_id, category_name='NO CATEGORY')