from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    from app.models import user

    db.init_app(app)
    migrate.init_app(app, db)

    return app