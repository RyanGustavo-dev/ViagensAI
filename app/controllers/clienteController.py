from app.bll.clienteBll import clienteBLL
from app.models.responseModels import Response
from flask import make_response, request, Blueprint

clientBP = Blueprint("cliente",__name__)
class clienteController:

    @clientBP.route("/user/create", methods=["POST"])
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
    