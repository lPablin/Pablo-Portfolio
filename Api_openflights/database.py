from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['openflights'] #Connect to the database

# Colecciones
airlines_collection = db['airlines']
airports_collection = db['airports']
countries_collection = db['countries']
planes_collection = db['planes']
routes_collection = db['routes']