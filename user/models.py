from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)
    api_key = db.Column(db.String(255), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    authenticated = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f'<User {self.id}: {self.username}>'

    def serailze(self):
        user_data = {
            'id': self.id,
            'username': self.username,
            'is_admin': self.is_admin,
            'is_active': self.is_active,
            'api_key': self.api_key
        }
        return user_data

