from marshmallow import ValidationError
from . import api
from flask import jsonify

@api.errorhandler(ValidationError)
def bad_request(e):
    response = jsonify({'status': 400, 'error': 'Bad Request',
                        'message': e.args[0]})
    response.status_code = 400
    return response

@api.errorhandler(404)
def not_found(e):
    response = jsonify({'status': 404, 'error': 'Not Found',
                        'message': 'Resource not found'})
    response.status_code = 404
    return response

@api.errorhandler(500)
def internal_server_error(e):
    response = jsonify({'status': 500, 'error': 'Internal Server Error',
                        'message': e.args[0]})
    response.status_code = 500
    return response

@api.errorhandler(401)
def invalid_credentials(e):
    response = jsonify({'status': 401, 'error': 'Invalid Credentials',
                        'message': e.args[0]})
    response.status_code = 401
    return response