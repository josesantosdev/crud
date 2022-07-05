from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serealize import configure as config_ma

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    
    config_db(app)
    config_ma(app)
    
    Migrate(app, app.db)
    
    from .books import bp_books
    app.register_blueprint(bp_books, url_prefix='/api/v1')
        
    return app

