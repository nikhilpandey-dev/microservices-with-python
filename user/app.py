from flask import Flask
from flask_migrate import Migrate
from routes import user_bp
from flask_login import LoginManager
import models

app = Flask(__name__)

app.config['SECRET_KEY'] = 'stI7qTToyA9XsIVUqdB2PA'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'

models.init_app(app)
# register blueprint
app.register_blueprint(user_bp)
# use Flask login manager for login management in the app
login_manager = LoginManager(app=app)

# Use flask migrate for database migrations
migrate = Migrate(app, models.db)


@login_manager.user_loader
def load_user(user_id):
    return models.db.session.query(models.User).filter_by(id=user_id).first()

@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic', '', 1)
        user = models.db.session.query(models.User).filter_by(api_key=api_key).first()
        if user:
            return user
    
    return None


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='