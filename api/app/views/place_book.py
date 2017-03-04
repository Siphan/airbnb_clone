"""Import app and models"""
from app import app
from app.models.place_book import PlaceBook
from app.models.place import Place

"""Import packages"""
from flask_json import jsonify, request

@app.route('/places/<place_id>/books', methods=['GET'])
def get_books(place_id):
    """Get a list of all bookings in the database"""

    books_query = PlaceBook.select().join(Place).where(Place.id == place_id)
    response = [i.to_hash() for i in books_query]

    if response:
        return jsonify(response)

    output = {'error': 'No results found'}
    response = jsonify(output)
    response.status_code = 404
    return response


@app.route('/places/<place_id>/books', methods=['POST'])
def post_book(place_id):
    """Create a new booking for a given place"""

    new_book = PlaceBook.create(
        place_id=place_id,
        user_id=request.form['user_id'],
        is_validated=request.form['is_validated'],
        date_start=request.form['date_start'],
        number_nights=request.form['number_nights']
    )
    return jsonify(new_book.to_hash())


@app.route('/places/<place_id>/books/<book_id>', methods=['GET'])
def get_book_by_id(place_id, book_id):
    """Get and return a given booking in the database"""

    book_query = PlaceBook.select().join(Place).where(Place.id == place_id, PlaceBook.id == book_id)
    response = [i.to_hash() for i in book_query]

    if response:
        return jsonify(response)

    output = {'error': 'No results found'}
    response = jsonify(output)
    response.status_code = 404
    return response


@app.route('/places/<place_id>/books/<book_id>', methods=['PUT'])
def update_book_by_id(place_id, book_id):
    """Modify a given booking in the database"""

    book_query = PlaceBook.select().join(Place).where(PlaceBook.id == book_id, Place.id == place_id).get()

    for key in request.values.keys():
        if key == 'is_validated':
            book_query.is_validated = request.values[key]
        elif key == 'date_start':
            book_query.date_start = request.values[key]
        elif key == 'number_nights':
            book_query.number_nights = request.values[key]
        elif key == 'user_id' or key == 'place_id':
            output = {'error': key + ' Not accepted'}
            error = jsonify(output)
            error.status_code = 400
            return error

    book_query.save()
    return jsonify(book_query.to_hash())


@app.route('/places/<place_id>/books/<book_id>', methods=['DELETE'])
def delete_book(place_id, book_id):
    """Delete a given booking from the database"""

    book_query = PlaceBook.select().join(Place).where(PlaceBook.id == book_id, Place.id == place_id).get()
    book_query.delete_instance()
    book_query.save()
    response = {'msg': 'Deleted book at id: ' + book_id}
    return jsonify(response)
