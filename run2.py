import pymongo
from config import *


URI_CONNECTION = "mongodb://%s:%s/" % (MONGODB_HOST, MONGODB_PORT)

try:
    client = pymongo.MongoClient(URI_CONNECTION)
    client.server_info()
    print('OK -- Connected to MongoDB at server %s' % (MONGODB_HOST))

    database_entry={'name':'John', 'surname':'Wick', 'city':'New York'}
    destination = 'PERSONAS'
    bd = client['TEST']
    coleccion = bd[destination]
    print(coleccion)
    coleccion.insert_one(database_entry)
    print("Data saved at %s collection in %s database: %s" % (destination, \
     'TEST', database_entry))
    client.close()
except Exception as error:
    print('Error with MongoDB connection: %s' % error)
