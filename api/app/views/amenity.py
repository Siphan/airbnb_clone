"""Import app and models"""
from app import app
from app.models.amenity import Amenity
from app.models.place_amenity import PlaceAmenities

"""Import packages"""
from flask_json import jsonify

@app.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity_by_id(amenity_id):
    """Get a list of all amenities in the database"""

    amenity_query = Amenity.get(Amenity.id == amenity_id)
    return jsonify(amenity_query.to_hash())


@app.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity_by_id(amenity_id):
    """Delete a given amenity from the database"""

    amenity_query = Amenity.get(Amenity.id == amenity_id)
    amenity_query.delete_instance()
    amenity_query.save()
    response = {'msg': 'deleted amenity at id: ' + amenity_id}
    return jsonify(response)


@app.route('/places/<place_id>/amenities', methods=['GET'])
def get_amenities_from_place(place_id):
    """Get and return a list of all amenities for a given accomodation"""

    amenity_query = Amenity.select().join(PlaceAmenities).where(PlaceAmenities.place == place_id)
    response = [i.to_hash() for i in amenity_query]

    if response:
        jsonify(response)

    output = {'error': 'No results found'}
    response = jsonify(output)
    response.status_code = 404
    return response
