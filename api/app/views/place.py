"""Import app and models"""
from app import app
from app.models.place import Place
from app.models.city import City

"""Import packages"""
from flask_json import jsonify, request

@app.route('/places', methods=['GET', 'POST'])
def places():
    """Get a list of all bookable accomodations in the database"""

    if request.method == 'GET':

        place_query = Place.select()
        response = [i.to_hash() for i in place_query]

        if response:
            return jsonify(response)

        error = {'error': 'No results found'}
        response = jsonify(error)
        response.status_code = 404
        return response

    elif request.method == 'POST':

        place = Place.create(
            owner_id=request.form['owner_id'],
            city_id=request.form['city_id'],
            name=request.form['name'],
            description=request.form['description'],
            number_rooms=request.form['number_rooms'],
            number_bathrooms=request.form['number_bathrooms'],
            max_guest=request.form['max_guest'],
            price_by_night=request.form['price_by_night'],
            latitude=request.form['latitude'],
            longitude=request.form['longitude']
        )
        return jsonify(place.to_hash())

@app.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'])
def put_places(place_id):
    """Update an accomodation in the database"""

    if request.method == 'GET':

        place_query = Place.get(Place.id == place_id)
        return jsonify(place_query.to_hash())

    elif request.method == 'PUT':

        place_query = Place.get(Place.id == place_id)

        for key in request.values.keys():
            if key == 'name':
                place_query.name = request.values[key]
            elif key == 'description':
                place_query.description = request.values[key]
            elif key == 'number_rooms':
                place_query.number_rooms = request.values[key]
            elif key == 'number_bathrooms':
                place_query.number_bathrooms = request.values[key]
            elif key == 'max_guest':
                place_query.max_guest = request.values[key]
            elif key == 'price_by_night':
                place_query.price_by_night = request.values[key]
            elif key == 'latitude':
                place_query.latitude = request.values[key]
            elif key == 'longitude':
                place_query.longitude = request.values[key]
            elif key == 'owner' or key == 'city':
                output = {'error': key + ' Not accepted'}
                error = jsonify(output)
                error.status_code = 400
                return error

        return jsonify(place_query.to_hash())

    elif request.method == 'DELETE':

        place_query = Place.get(Place.id == place_id)
        place_query.delete_instance()
        place_query.save()
        response = {'msg': 'Deleted place at id: ' + place_id}
        return jsonify(response)

@app.route('/states/<state_id>/cities/<city_id>/places', methods=['GET', 'POST'])
def get_city_places(state_id, city_id):
    """Get a list of all accomodations in a given city in the database"""

    if request.method == 'GET':

        place_query = Place.select().join(City).where(City.id == city_id, City.state == state_id)
        response = [i.to_hash() for i in place_query]

        if response:
            return jsonify(response)

        output = {'error': 'No results found'}
        response = jsonify(output)
        response.status_code = 404
        return response

    elif request.method == 'POST':

        place = Place.create(
            owner_id=request.form['owner_id'],
            city_id=city_id,
            name=request.form['name'],
            description=request.form['description'],
            number_rooms=request.form['number_rooms'],
            number_bathrooms=request.form['number_bathrooms'],
            max_guest=request.form['max_guest'],
            price_by_night=request.form['price_by_night'],
            latitude=request.form['latitude'],
            longitude=request.form['longitude']
        )
        return jsonify(place.to_hash())
