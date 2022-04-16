from flask import request
from flask_restplus import Resource

from server.instance import server
from models.pix import PixModel

api = server.api


@api.route('/orders', methods=['POST'])
class Pix(Resource):

    def post(self, ):
        payload = request.json
        txid = payload.pop('txid')

        pix_model = PixModel()
        response = pix_model.create_charge(txid, payload)

        return response
