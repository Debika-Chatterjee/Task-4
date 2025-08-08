from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user store
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET a specific user
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    if username in users:
        return jsonify({'error': 'User already exists'}), 400
    users[username] = data
    return jsonify({'message': 'User created'}), 201

# PUT to update user
@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    users[username].update(data)
    return jsonify({'message': 'User updated'})

# DELETE a user
@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    if username in users:
        del users[username]
        return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
