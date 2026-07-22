from app.models.responseModels import Response
from flask import make_response, request, Blueprint
from app.bll.excursaoBll import ExcursaoBLL

excursaoBP = Blueprint("excursao",__name__)

class ExcursaoController:

    @excursaoBP.route("/excursoes", methods=["POST"])
    def createExcursao():
        try:
            data = request.json
            bll = ExcursaoBLL()
    
            resultado = bll.createNewExcusao(data)
    
            response = Response(201, "", resultado)
            return make_response(response.toDict(), 201)
        
        except Exception as e:

            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)

    @excursaoBP.route("/excursoes", methods=["GET"])
    def getAllExcursao():
        try:
            date_start = request.args.get("date_start")
            date_end = request.args.get("date_end")
            destino_id = request.args.get("destino_id")
            codigo = request.args.get("codigo")
            bll = ExcursaoBLL()

            resultado = bll.getAllExcursao(date_start,date_end,destino_id,codigo)
            return make_response(200, resultado)
        
        except Exception as e:

            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)

    @excursaoBP.route("/excursoes/<id>",methods=["GET"])
    def getExcursaoById(id):
        try:
            bll = ExcursaoBLL()
            resultado = bll.getExcursaoById(id)
            return make_response(200, resultado)
        
        except Exception as e:
        
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)

    @excursaoBP.route("/excursoes/<id>", methods=["PUT"])
    def updateExcursao(id):
        try:
            data = request.json
            bll = ExcursaoBLL()
            resultado = bll.editExcursao(id, data)
            response = Response(201, "", resultado)
            return make_response(response.toDict(), 201)
        
        except Exception as e:

            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)

    @excursaoBP.route("/excursoes/<id>", methods=["DELETE"])
    def deleteExcursao(id):
        try:
            bll = ExcursaoBLL()
            resultado = bll.deleteExcursao(id)
            response = Response(201, "", resultado)
            return make_response(response.toDict(), 201)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)

    @excursaoBP.route("/excursoes/<id>/lista-passageiros", methods=["GET"])
    def getListaPassageiro(id):
        try:
            bll = ExcursaoBLL()
            resultado = bll.getListaPassageiros(id)
            return make_response(200, resultado)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)

    @excursaoBP.route("/excursoes/<id>/assentos", methods=["GET"])
    def getListaAssentos(id):
        try:
            bll = ExcursaoBLL()
            resultado = bll.getListaAssentos(id)
            return make_response(200, resultado)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)