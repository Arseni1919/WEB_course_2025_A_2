import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://1919ars:1919ars@cluster0.kg52uoz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new cluster and connect to the server
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['mydatabase']
customers_col = mydatabase['customers']
products_col = mydatabase['products']
products_col = mydatabase['products']
products_col = mydatabase['products']
products_col = mydatabase['products']
products_col = mydatabase['products']



def customer_update(my_dict):
    # insert_one
    customers_col.insert_one(my_dict)