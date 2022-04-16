import base64
import json
import requests
import pyqrcode
from PIL import Image
from io import BytesIO
from flask import send_file

from utils.constants import *

from gerencianet import Gerencianet as gn


class PixModel():
    def __init__(self):
        self.headers = {
            'Authorization': f'Basic {self.get_token()}',
            'Content-Type': 'application/json'
        }

    def get_token(self, ):
        auth = base64.b64encode(f'{CLIENT_ID_HOM}:{CLIENT_SECRET_HOM}'.encode()).decode()

        headers = {
            'Authorization': f'Basic {auth}',
            'Content-Type': 'application/json'
        }

        payload = {"grant_Type": "client_credentials"}

        response = requests.post(f'{URL_HOM}/oauth/token', headers=headers, data=json.dumps(payload), cert=CERT_HOM)

        return json.loads(response.content)['access_token']

    def create_qrcode(self, location_id):
        response = requests.get(
            f'{URL_HOM}/v2/loc/{location_id}/qrcode', headers=self.headers, cert=CERT_HOM
        )

        json.loads(response.content)

    def create_order(self, txid, payload):
        response = requests.put(
            f'{URL_HOM}/v2/loc/{txid}/qrcode', data=json.dumps(payload), headers=self.headers, cert=CERT_HOM
        )

        if response.status_code == 201:
            return json.loads(response.content)

        return {}

    def qrcode_generator(self, location_id):
        qrcode = self.create_qrcode(location_id)

        data_qrcode = qrcode['qrcode']

        url = pyqrcode.QRCode(data_qrcode, error='H')
        url.png('qrcode.jpg', scale=10)
        im = Image.open('qrcode.jpg')
        im = im.convert('RGBA')
        img_io = BytesIO()
        im.save(img_io, 'PNG', quality=100)
        img_io.seek(0)

        return send_file(img_io, mimetype='image/jpeg', as_attachment=False, attachment_filename='image-qrcode.jpg')

    def create_charge(self, txid, payload):
        location_id = self.create_order(txid, payload).get('loc').get('id')
        qrcode = self.qrcode_generator(location_id)

        return qrcode
