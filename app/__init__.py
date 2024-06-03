from flask import Flask
# HAY QUE ELIMINARLOS DE AQUI PORQUE GENERAN REFERENCIAS CIRCULARES
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# db = SQLAlchemy()
# migrate = Migrate()
from app.database import db
from app.extensions import migrate,marshmallow
from app.private import private_bp 
from flask_restful import Api


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    Api(app)
    
    # blueprints
    app.register_blueprint(private_bp)
    
    return app
    