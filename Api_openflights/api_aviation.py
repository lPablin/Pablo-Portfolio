from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['openflights']

# Colecciones
airlines_collection = db['airlines']
airports_collection = db['airports']
countries_collection = db['countries']
planes_collection = db['planes']
routes_collection = db['routes']

@app.route('/')
def index():
    return "Welcome to the Aviation API"

# Rutas para aerolíneas
@app.route('/airlines', methods=['GET'])
def get_airlines():
    airlines = list(airlines_collection.find())
    for airline in airlines:
        airline['_id'] = str(airline['_id'])
    return jsonify(airlines)

@app.route('/airlines/<id>', methods=['GET'])
def get_airline(id):
    airline = airlines_collection.find_one({'_id': ObjectId(id)})
    if airline:
        airline['_id'] = str(airline['_id'])
        return jsonify(airline)
    else:
        return jsonify({'error': 'Airline not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)