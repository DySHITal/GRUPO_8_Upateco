from werkzeug.exceptions import HTTPException
from flask import jsonify


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

class FilmNotFound(CustomException):
    def __init__(self, film_id):
        self.film_id = film_id
        super().__init__(status_code=404, name='Film Not Found')

    def get_response(self):
        return jsonify({
            'error':{
                'error': 404,
                'name': 'Film Not Found',
                'description': f'La película con el ID: {self.film_id} no se encuentra'
            }  
        })

class InvalidDataError(CustomException):
    def __init__(self, description = 'Dato Invalido'):
        super().__init__(status_code = 403, name='InvalidData', description=description)