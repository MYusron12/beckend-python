from flask import Blueprint, request, jsonify # type: ignore
from controllers.user_controller import UserController

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user_data = UserController.fetch_user(user_id)
    if user_data:
        return jsonify({"status": "success", "data": user_data}), 200
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404

@user_blueprint.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = UserController.create_user(data['name'], data['email'])
    return jsonify({"status": "success", "user_id": user_id}), 201

@user_blueprint.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    success = UserController.update_user(user_id, data['name'], data['email'])
    if success:
        return jsonify({"status": "success", "message": "User updated"}), 200
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404

@user_blueprint.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = UserController.delete_user(user_id)
    if success:
        return jsonify({"status": "success", "message": "User deleted"}), 200
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404
