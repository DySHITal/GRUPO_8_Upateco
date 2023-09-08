from ..models.film_model import Film
from ..models.exceptions import FilmNotFound, InvalidDataError
from flask import request

from decimal import Decimal

class FilmController:
    """Film controller class"""

    @classmethod
    def get(cls, film_id):
        """Get a film by id"""
        film = Film(film_id=film_id)
        result = Film.get(film)
        if result is not None:
            return result.serialize(), 200
        else:
            error = FilmNotFound(film_id)
            return error.get_response(), 404
        
    @classmethod
    def get_all(cls):
        """Get all films"""
        film_objects = Film.get_all()
        films = []
        for film in film_objects:
            films.append(film.serialize())
        return films, 200
    
    @classmethod
    def create(cls):
        """Create a new film"""
        data = request.json
        # TODO: Validate data
        if data.get('title') is not None:
            if len(data.get('title', '')) < 3:
                error = InvalidDataError('El título debe tener al menos 3 caracteres')
                return error.get_response(), 400 
        else:
            error = InvalidDataError('El título es obligatorio') 
            return error.get_response(), 400

        if data.get('language_id') is not None:
            if not isinstance(data.get('language_id'), int):
                error = InvalidDataError('El ID del idioma debe ser un número entero')
                return error.get_response(), 400
        else:
            error = InvalidDataError('El ID del idioma es obligatorio') 
            return error.get_response(), 400

        if data.get('rental_duration') is not None:
            if not isinstance(data.get('rental_duration'), int):
                error = InvalidDataError('La duración del alquiler debe ser un número entero')
                return error.get_response(), 400
        else:
            error = InvalidDataError('La duración del alquiler es obligatorio') 
            return error.get_response(), 400

        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
            else:
                error = InvalidDataError('El precio del alquiler debe ser un número entero')
                return error.get_response(), 400
        else:
            error = InvalidDataError('El precio del alquiler es obligatorio') 
            return error.get_response(), 400
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
            else:
                error = InvalidDataError('El costo del reemplazo debe ser un número entero')
                return error.get_response(), 400
        else:
            error = InvalidDataError('El costo del alquiler es obligatorio') 
            return error.get_response(), 400

        if data.get('special_features') is not None:
            special_features = ["Trailers", "Commentaries", "Deleted Scenes", "Behind the Scenes"]
            if not isinstance(data.get('special_features', list)):
                error = InvalidDataError('Las características especiales deben ser una lista de cadenas')
                return error.get_response(), 400
            else:
                for feature in data.get('special_features'):
                    if feature not in special_features:
                        error = InvalidDataError(f'La característica especial {feature} es invalida')
                        return error.get_response(), 400
        else:
            error = InvalidDataError('Las características especiales son obligatorias')
            return error.get_response(), 400

        film = Film(**data)
        Film.create(film)
        return {'message': 'Film created successfully'}, 201

    @classmethod
    def update(cls, film_id):
        """Update a film"""
        data = request.json
        # TODO: Validate data
        if data.get('title') is not None:
            if len(data.get('title', '')) < 3:
                error = InvalidDataError('El título debe tener al menos 3 caracteres')
                return error.get_response(), 400 
        else:
            error = InvalidDataError('El título es obligatorio') 
            return error.get_response(), 400

        if data.get('language_id') is not None:
            if not isinstance(data.get('language_id'), int):
                error = InvalidDataError('El ID del idioma debe ser un número entero')
                return error.get_response(), 400
        else:
            error = InvalidDataError('El ID del idioma es obligatorio') 
            return error.get_response(), 400

        if data.get('rental_duration') is not None:
            if not isinstance(data.get('rental_duration'), int):
                error = InvalidDataError('La duración del alquiler debe ser un número entero')
                return error.get_response(), 400
        else:
            error = InvalidDataError('La duración del alquiler es obligatorio') 
            return error.get_response(), 400

        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
            else:
                error = InvalidDataError('El precio del alquiler debe ser un número entero')
                return error.get_response(), 400
        else:
            error = InvalidDataError('El precio del alquiler es obligatorio') 
            return error.get_response(), 400
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
            else:
                error = InvalidDataError('El costo del reemplazo debe ser un número entero')
                return error.get_response(), 400
        else:
            error = InvalidDataError('El costo del alquiler es obligatorio') 
            return error.get_response(), 400

        if data.get('special_features') is not None:
            special_features = ["Trailers", "Commentaries", "Deleted Scenes", "Behind the Scenes"]
            if not isinstance(data.get('special_features', list)):
                error = InvalidDataError('Las características especiales deben ser una lista de cadenas')
                return error.get_response(), 400
            else:
                for feature in data.get('special_features'):
                    if feature not in special_features:
                        error = InvalidDataError(f'La característica especial {feature} es invalida')
                        return error.get_response(), 400
        else:
            error = InvalidDataError('Las características especiales son obligatorias')
            return error.get_response(), 400
        
        data['film_id'] = film_id

        film = Film(**data)

        # TODO: Validate film exists
        if not film.exists:
            error = FilmNotFound(film_id)
            return error.get_response(), 404
        Film.update(film)
        return {'message': 'Film updated successfully'}, 200
    
    @classmethod
    def delete(cls, film_id):
        """Delete a film"""
        film = Film(film_id=film_id)

        # TODO: Validate film exists
        if not film.exists:
            error = FilmNotFound(film_id)
            return error.get_response(),404
        Film.delete(film)
        return {'message': 'Film deleted successfully'}, 204