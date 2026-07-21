import os
from flask import Flask
from app.extension import db, migrate, createControllers
from app.config.settings import config_map

def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_map[env])
    

    db.init_app(app)
    migrate.init_app(app, db)

    #REGISTRAR BLUEPRINTS
    createControllers(app)

    return app