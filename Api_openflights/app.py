from flask import Flask, jsonify, request, render_template
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Airlines table
@app.route('/airlines', methods=['GET'])
def get_airlines():
    #Airlines from the database
    airlines = list(airlines_collection.find())

    formatted_airlines = []
    for airline in airlines:
        formatted_airline = {
            'id': str(airline['_id']),
            'name': airline.get('name', ''),
            'iataCode': airline.get('iataCode', ''),
            'icaoCode': airline.get('icaoCode', ''),
            'callsign': airline.get('callsign', ''),
            'country': airline.get('country', ''),
            'active': airline.get('active', '')
        }
        formatted_airlines.append(formatted_airline)
    return render_template('index_airlines.html', airlines=formatted_airlines)#table with the data

# Airlines table
@app.route('/planes', methods=['GET'])
def get_planes():
    #Airlines from the database
    planes = list(planes_collection.find())

    formatted_planes = []
    for plane in planes:
        formatted_plane = {
            'id': str(plane['_id']),
            'Aircraft_Name': plane.get('Aircraft_Name', ''),
            'IATA_Code': plane.get('IATA_Code', ''),
            'ICAO_Code': plane.get('ICAO_Code', ''),
        }
        formatted_planes.append(formatted_plane)

    return render_template('index_planes.html', planes=formatted_planes)#table with the data
 
#get all the airports
@app.route('/airports')
def get_airports():
    # Obtener todos los aeropuertos de la colección
    airports = list(airports_collection.find())

    # Formatear los datos para la tabla
    formatted_airports = []
    for airport in airports:
        formatted_airport = {
            'id': str(airport['_id']),
            'City': airport.get('City', ''),
            'Country': airport.get('Country', ''),
            'ICAO': airport.get('ICAO', ''),
            'Latitude': round(float(airport.get('Latitude', 0)), 3) if 'Latitude' in airport else '',
            'Longitude': round(float(airport.get('Longitude', 0)), 3) if 'Longitude' in airport else '',
            'Altitude': airport.get('Altitude', ''),
            'Timezone': airport.get('Timezone', '')
        }
        formatted_airports.append(formatted_airport)

    return render_template('index_airports.html', airports=formatted_airports)#table with the data

@app.route('/airportsmap')#it's for having a json for the map
def get_airports_map():
    country = request.args.get('country', 'none')
    
    if country == 'none':
        airports = []  # empty list for avoiding load all the airports the first time
    else:
        airports = list(airports_collection.find({'Country': country}))

    formatted_airports = [{
        'Name': airport.get('Name', ''),
        'City': airport.get('City', ''),
        'Country': airport.get('Country', ''),
        'Latitude': round(float(airport.get('Latitude', 0)), 2),
        'Longitude': round(float(airport.get('Longitude', 0)), 2),
    } for airport in airports]

    return jsonify(formatted_airports)
""""
#get airports by id
@app.route('/airports/<Airport_ID>', methods=['GET'])
def get_airport(Airport_ID):
    airport = airports_collection.find_one({'_id': ObjectId(Airport_ID)})
    if airport:
        airport['Airport_ID'] = str(airport['Airport_ID'])
        return jsonify(airport)
    else:
        return jsonify({'error': 'Airport not found'}), 404
"""
@app.route('/map')
def airports_map():
    return render_template('index_map_country.html')

@app.route('/countries')
def get_countries():
    countries = airports_collection.distinct("Country")
    return jsonify(countries)

@app.route('/airports_in_country')
def get_airports_in_country():
    country = request.args.get('country', 'none')
    
    if country == 'none':
        airports = []
    else:
        airports = list(airports_collection.find({'Country': country}))
    
    formatted_airports = [{
        'Name': airport.get('Name', ''),
        'IATA': airport.get('IATA', ''),
        'Latitude': round(float(airport.get('Latitude', 0)), 2),
        'Longitude': round(float(airport.get('Longitude', 0)), 2),
    } for airport in airports]

    return jsonify(formatted_airports)

@app.route('/routes')
def get_routes():
    source = request.args.get('source', 'none')
    country = request.args.get('country', 'none')
    
    if source == 'none':
        routes = []
    elif source == 'all' and country != 'none':
        # Encontrar todos los aeropuertos del país seleccionado con coordenadas válidas
        airports_in_country = list(airports_collection.find({
            'Country': country,
            'Latitude': {'$exists': True, '$ne': ''},
            'Longitude': {'$exists': True, '$ne': ''}
        }, {'IATA': 1, 'Latitude': 1, 'Longitude': 1}))
        
        iata_list = [airport['IATA'] for airport in airports_in_country]
        
        # Encontrar todas las rutas cuyo aeropuerto de origen esté en la lista de IATA
        routes = list(routes_collection.find({'Source Airport (IATA)': {'$in': iata_list}}))
    else:
        # Solo filtra rutas del aeropuerto seleccionado
        routes = list(routes_collection.find({'Source Airport (IATA)': source}))

    # Formatear las rutas asegurando que ambos aeropuertos tengan coordenadas válidas
    formatted_routes = []
    for route in routes:
        source_airport = airports_collection.find_one({
            'IATA': route['Source Airport (IATA)'],
            'Latitude': {'$exists': True, '$ne': ''},
            'Longitude': {'$exists': True, '$ne': ''}
        })
        dest_airport = airports_collection.find_one({
            'IATA': route['Destination Airport (IATA)'],
            'Latitude': {'$exists': True, '$ne': ''},
            'Longitude': {'$exists': True, '$ne': ''}
        })
        if source_airport and dest_airport:
            formatted_routes.append({
                'source': {
                    'Latitude': source_airport['Latitude'],
                    'Longitude': source_airport['Longitude']
                },
                'destination': {
                    'Latitude': dest_airport['Latitude'],
                    'Longitude': dest_airport['Longitude']
                }
            })

    return jsonify(formatted_routes)


@app.route('/maproutes')
def routes_map():
    return render_template('index_map_routes.html')

if __name__ == '__main__':
    app.run(debug=True)