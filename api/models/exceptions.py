from flask import jsonify
from werkzeug.exceptions import HTTPException

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
class UsuarioNotFound(CustomException):
    def __init__(self, film_id):
        super().__init__(status_code=401, name="Usuario Not Found", description=f"Usuario with id {film_id} not found")

class InvalidDataError(CustomException):
    def __init__(self, description):
        super().__init__(status_code=400, name="Invalid Data", description=description)   

