from config import Config
from neil_app import NeilApp


def create_app():
    app = NeilApp(__name__)
    app.config.from_object(Config)
    init_extensions(app)
    return app
    

def init_extensions(app: NeilApp):
    from extensions import (
        ext_mysql,
        ext_blueprints
    )
    
    extensions = [
        ext_mysql,
        ext_blueprints
    ]
    for ext in extensions:
        ext.init_app(app)