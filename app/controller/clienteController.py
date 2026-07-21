from bll.clienteBll import clienteBLL
from models.responseModels import Response
from run import app
from flask import make_response, request


class clienteController:

    @app.route("/user/create", methods=["POST"])
    def createNewUser():
        try:
            data = request.json
            bll = clienteBLL()

            resultado = bll.createNewCliente(data)

            response = Response(200, "", resultado)
            return make_response(response.toDict(), 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(),400)
    