from flask_restplus import Resource

from server.instance import server
from models.pix import PixModel

api = server.api


@api.route('/token', methods=['POST'])
class Token(Resource):
    def post(self, ):
        pix_model = PixModel
        response = pix_model.get_token()

        return response
