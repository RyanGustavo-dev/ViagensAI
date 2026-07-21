from app.bll.enderecoBll import EnderecoBLL
from app.models.responseModels import Response
from flask import make_response, request, Blueprint

enderecoBP = Blueprint("endereco",__name__)

class EnderecoController:
    @enderecoBP.route("/enderecos", methods=["POST"])
    def createNewEndereco():
        try:
            data = request.json
            bll = EnderecoBLL()

            resultado = bll.createNewEndereco(data)
            response = Response(201, "", resultado)
            return make_response(response.toDict(), 201)
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)
    
    @enderecoBP.route("/enderecos", methods=["GET"])
    def getAllEndereco():
        try:
            bll = EnderecoBLL()

            resultado = bll.getAllEnderecos()
            return make_response(resultado, 200)
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)
        
    @enderecoBP.route("/enderecos/<id>", methods=["GET"])
    def getEnderecoById(id):
        try:
            bll = EnderecoBLL()

            resultado = bll.getEnderecoById(id)
            return make_response(resultado, 200)
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)

    @enderecoBP.route("/enderecos/<id>", methods=["PUT"])
    def editEndereco(id):
        try:
            data = request.json

            bll = EnderecoBLL()

            result = bll.editEndereco(id, data)
            response = Response(200, "", result)
            return make_response(response.toDict(), 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)
    
    @enderecoBP.route("/enderecos/<id>", methods=["DELETE"])
    def deleteEnderecoByID(id):
        try:
            bll = EnderecoBLL()

            result = bll.deleteEndereco(id)
            response = Response(200, "", result)
            return make_response(response.toDict(),200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)