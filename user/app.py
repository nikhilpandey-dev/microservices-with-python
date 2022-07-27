from flask import Flask
from routes import user_bp
import models

app = Flask(__name__)

app.config['SECRET_KEY'] = 'stI7qTToyA9XsIVUqdB2PA'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = FALSE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'

models.init_app(app)

app.register_blueprint(user_bp)


app.run()