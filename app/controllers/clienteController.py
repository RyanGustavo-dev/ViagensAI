from app.bll.clienteBll import clienteBLL
from app.models.responseModels import Response
from flask import make_response, request, Blueprint

clientBP = Blueprint("cliente",__name__)
class clienteController:

    @clientBP.route("/clientes", methods=["POST"])
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
    
    @clientBP.route("/clientes", methods=["GET"])
    def getClient():
        try:
            nome = request.args.get("nome")
            cpf = request.args.get("cpf")

            bll = clienteBLL()

            resultado = bll.getClientByCpfOrNome(nome, cpf)
            return make_response(resultado, 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(),400)

    @clientBP.route("/clientes/<id>", methods=["PUT"])
    def updateClient(id):
        try:
            data = request.json
            bll = clienteBLL()

            resultado = bll.updateClient(id, data)
            response = Response(200, "", resultado)
            return make_response(response.toDict(), 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(),400)

    @clientBP.route("/clientes/<id>", methods=["DELETE"])
    def deleteClient(id):
        try:
            bll = clienteBLL()

            resultado = bll.deleteClient(id)
            response = Response(200, "", resultado)
            return make_response(response.toDict(), 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(),400)