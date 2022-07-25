from flask import Flask
from routes import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)


app.run()