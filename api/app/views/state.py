"""Import app and models"""
from app import app
from app.models.state import State

"""Import packages"""
from flask_json import jsonify, request


@app.route('/states', methods=['GET', 'POST'])
def states():
    """Get a list of all states in the database."""

    if request.method == 'GET':

        state_query = State.select()
        response = [i.to_hash() for i in state_query]

        if response:
            return jsonify(response)
        else:
            output = {'error': 'No results found'}
            response = jsonify(output)
            response.status_code = 404
            return response

    elif request.method == 'POST':

        duplicate_name = State.select().where(State.name == request.form['name'])

        if not duplicate_name:

            state = State.create(
                name=request.form['name']
            )
            return jsonify(state.to_hash())


        output = {'code': 10001, 'msg': 'State already exists'}
        response = jsonify(output)
        response.status_code = 409
        return response

@app.route('/states/<state_id>', methods=['GET', 'DELETE'])
def states_id(state_id):
    """Return the id of a given state"""

    if request.method == 'GET':

        state_query = State.get(State.id == state_id)
        return jsonify(state_query.to_hash())

    elif request.method == 'DELETE':

        state_query = State.get(State.id == state_id)
        state_query.delete_instance()
        state_query.save()
        response = {'msg': 'Deleted state at id: ' +  state_id }
        return jsonify(response)
