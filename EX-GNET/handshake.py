from flask import Flask, jsonify, request
import ssl
import json
app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/", methods=["PUT"])
def hello_put():
    response = {"status": 200}
    return jsonify(response)


@app.route("/", methods=["POST"])
def imprimir():
    imprime = print(request.json)
    data = request.json
    with open('data.txt', 'a') as outfile:
        outfile.write("\n")
        json.dump(data, outfile)
    return jsonify(imprime)

def hello_post():
    response = {"status": 200}
    return jsonify(response)

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations('caminho-certificados/certificado-público-Gerencianet.crt')
    context.load_cert_chain(
        'caminho-certificados/server_ssl.crt.pem',
        'caminho-certificados/server_ssl.key.pem')
    app.run(ssl_context=context, host='0.0.0.0')