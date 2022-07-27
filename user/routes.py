from distutils.log import error
import sqlite3
from flask import Blueprint, jsonify, request
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
user_bp = Blueprint('user_api_routes', __name__,url_prefix='/api/user')


@user_bp.route('/all')
def get_all_users():
    all_users = db.session.query(User).all()
    result = [user.serialize() for user in all_users]
    response = {
        'message': 'Successfully retrieved all users',
        'result': result
    }
    return jsonify(response)


@user_bp.route('/create', methods=['POST'])
def create_user():
    try:
        user = User()
        user.username = request.form["username"]
        user.password = generate_password_hash(request.form["password"], method='sha256')
        user.is_admin = True
        
        db.session.add(user)
        db.session.commit()
        
        response = {'message': 'user created successfully', 'result': user.serialize()}
    except Exception as e:
        print(str(e))
        error_msg = f'Error in creating user: {e.args[0]}'
        response = {'message': error_msg}
        
    return jsonify(response)