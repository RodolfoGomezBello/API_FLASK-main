from flask import Flask, session
from flask_cors import CORS

from config import Config

from .routes.usuariosroutes import usuarios_routes

from .database import DatabaseConnection

from .routes.error_handlers import errors

#from .controllers import mail

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )
    
    app.config['JSON_AS_ASCII'] = False
    DatabaseConnection.set_config(app.config)

    # Inicializa la extensión Mail con la aplicación Flask usando la instancia pasada como argumento
   # mail.init_app(app)   

    app.register_blueprint(usuarios_routes, url_prefix = '/usuarios')
    app.register_blueprint(errors, url_prefix = '/errors')


    return app
