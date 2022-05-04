from flask import Flask, request, Response, json
from flask_cors import cross_origin

import application.utils.responses as responses
from application.utils.validator_request import game_validator
from domain.exceptions.custom_exception import CustomException
from domain.services.game_service_v2 import GameService

app = Flask(__name__)
service = GameService()


@app.route('/')
@cross_origin()
def home():
    return _send_response(responses.WELCOME, 200)


@app.route('/api/game', methods=['POST'])
@cross_origin()
def game():
    config_game = request.get_json()
    if game_validator.validate(config_game):
        return _send_response(service.get_slides_game(config_game), 200)
    else:
        return _send_response(responses.INVALID_REQUEST, 400)


@app.errorhandler(404)
def page_not_found(_):
    return _send_response(responses.NOT_FOUND_ENDPOINT, 404)


@app.errorhandler(500)
def internal_error(_):
    return _send_response(responses.INTERNAL_SERVER_ERROR, 500)


@app.errorhandler(CustomException)
def custom_exception(error):
    return _send_response({'timestamp': error.timestamp, 'message': error.message}, error.status_code)


def _send_response(response_p, status):
    return Response(json.dumps(response_p), status=status, mimetype='application/json')


if __name__ == '__main__':
    app.run()
