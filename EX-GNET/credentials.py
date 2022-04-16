# encoding: utf-8

from gerencianet import Gerencianet

credentials = {
    'client_id': 'Client_Id_5e91a758a6a345267fbf4e94cf90fab049220997',
    'client_secret': 'Client_Secret_3716c3493a46287e47617504a9c30b69e112a165',
    'pix_cert': 'certificado.pem',
    'sandbox': True
}

gn = Gerencianet(credentials)

body = {
    'items': [
        {
            'id': "01",
            'name': "Product 1",
            'value': 1000,
            'portion': 25,
            'stock': 2000
        },
        {
            'id': "02",
            'name': "Product 2",
            'value': 1200,
            'portion': 50,
            'stock': 2000
        }
    ],
    'shippings': [
        {
            'name': "Default Shipping Cost",
            'value': 100
        }
    ]
}

print(gn.create_charge(body=body))
