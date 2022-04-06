import pymongo
from config import *


URI_CONNECTION = "mongodb://%s:%s/" % (MONGODB_HOST, MONGODB_PORT)

try:
    client = pymongo.MongoClient(URI_CONNECTION)
    client.server_info()
    print('OK -- Connected to MongoDB at server %s' % (MONGODB_HOST))
    client.close()
except pymongo.errors.ServerSelectionTimeoutError as error:
    print('Error with MongoDB connection: %s' % error)
except pymongo.errors.ConnectionFailure as error:
    print('Could not connect to MongoDB: %s' % error)
