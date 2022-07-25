from flask import Blueprint

user_bp = Blueprint('user_api_routes', __name__,url_prefix='/api/user')


@user_bp.route('/')
def index():
    return "Hello World from Blueprint!"