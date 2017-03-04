"""Import app and models"""
from app import app
from app.models.user import User

"""Import packages"""
from flask_json import jsonify, request

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    """Get list of all users in the database"""

    if request.method == 'GET':

        user_query = User.select()
        response = [i.to_hash() for i in user_query] #<---

        if response:
            return jsonify(response)

        output = {'error': 'No results found'}
        response = jsonify(output)
        response.status_code = 404
        return response

    elif request.method == 'POST':

        duplicate_email = User.select().where(User.email == request.form['email'])

        if not duplicate_email:

            user = User.create(
                email=request.form['email'],
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                password=""
            )

            user.set_password(request.form['password'])
            return jsonify(user.to_hash())


        output = {'code': 10000, 'msg': 'Email already exists'}
        response = jsonify(output)
        response.status_code = 409
        return response

@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_users_id(user_id):
    """Get the given user id"""

    if request.method == 'GET':
        user_query = User.get(User.id == user_id)
        return jsonify(user_query.to_hash())

    elif request.method == 'PUT':

        for key in request.values.keys():
            if key == 'id':
                user_query.id = request.values[key]
            elif key == 'first_name':
                user_query.first_name = request.values[key]
            elif key == 'last_name':
                user_query.last_name = request.values[key]
            elif key == 'is_admin':
                user_query.is_admin = request.values[key]
            elif key == 'email' or key == 'created_at' or key == 'updated_at':
                output = {'error': key + ' Not accepted'}
                error = jsonify(output)
                error.status_code = 400
                return error

        user_query.save()
        return jsonify(user_query.to_hash())

    elif request.method == 'DELETE':

        user_query = User.get(User.id == user_id)
        user_query.delete_instance()
        user_query.save()
        response = {'msg': 'Deleted user at id: ' +  user_id }
        return jsonify(response)
