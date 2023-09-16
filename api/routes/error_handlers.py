from flask import Blueprint
from ..models.exceptions import  UsuarioNotFound, InvalidDataError, MensajeNotFound
errors = Blueprint("errors", __name__)

@errors.app_errorhandler(UsuarioNotFound)
def handle_film_not_found(error):
   return error.get_response(), error.status_code

@errors.app_errorhandler(InvalidDataError)
def handle_invalid_data(error):
    return error.get_response(), error.status_code


@errors.app_errorhandler(MensajeNotFound)
def handle_film_not_found(error):
   return error.get_response(), error.status_code

