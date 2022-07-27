from flask import Flask
from flask_migrate import Migrate
from routes import user_bp
import models

app = Flask(__name__)

app.config['SECRET_KEY'] = 'stI7qTToyA9XsIVUqdB2PA'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'

models.init_app(app)

app.register_blueprint(user_bp)

migrte = Migrate(app, models.db)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='