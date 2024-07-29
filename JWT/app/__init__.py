from flask import Flask
from app.auth import auth
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    with app.app_context():
        import app.models
        app.register_blueprint(auth, url_prefix='/auth')
        
    return app