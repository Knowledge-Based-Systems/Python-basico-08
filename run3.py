import pymongo
from config import *


URI_CONNECTION = "mongodb://%s:%s/" % (MONGODB_HOST, MONGODB_PORT)

try:
    client = pymongo.MongoClient(URI_CONNECTION)
    client.server_info()
    print('OK -- Connected to MongoDB at server %s' % (MONGODB_HOST))
    destination = 'PERSONAS'
    bd = client['TEST']
    coleccion = bd[destination]
    print(coleccion)
    datos = coleccion.find()
    for d in datos:
        print(d)
        print(d.__class__)
    client.close()
except Exception as error:
    print('Error with MongoDB connection: %s' % error)
