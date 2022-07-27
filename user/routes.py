from distutils.log import error
from tabnanny import check
import sqlite3
from flask import Blueprint, jsonify, request, make_response
from flask_login import login_user, current_user, logout_user
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


@user_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = db.session.query(User).filter_by(username=username).first()
    
    if not user:
        response = {'message': 'username or password does not exists!'}
        return make_response(jsonify(response), 401)

    if check_password_hash(user.password, password):
        user.update_api_key()
        db.session.commit()
        login_user(user=user)
        response = {
            'message': 'logged in',
            'api_key': user.api_key
        }
        return make_response(jsonify(response), 200)
    
    response = {'message': 'Access denied'}
    return make_response(jsonify(response), 401)


@user_bp.route('/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'logged out'})
    return jsonify({{'message': 'No user logged in'}}), 401

@user_bp.route('/<username>/exists')
def user_exists(username):
    user = db.session.query(User).filter_by(username=username).first()
    if user:
        return jsonify({'result': True}), 200
    
    return jsonify({'result': False}), 404

@user_bp.route('/')
def get_current_user():
    if current_user.is_authenticated:
        return jsonify({'result': current_user.serialize()}), 200
    else:
        return jsonify({'message': "User not logged in"}), 401
    


  
  
        
    

