from app.bll.onibusBll import OnibusBll
from app.models.responseModels import Response
from flask import make_response, request, Blueprint

onibusBP = Blueprint("onibus",__name__)

class OnibusController:

    @onibusBP.route("/onibus", methods=["POST"])
    def createNewUser():
        try:
            data = request.json
            bll = OnibusBll()

            result = bll.createNewOnibus(data)
            response = Response(201, "", result)
            return make_response(response.toDict(), 201)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)

    @onibusBP.route("/onibus", methods=["GET"])
    def getAllOnibus():
        try:
            bll = OnibusBll()

            result = bll.getAllOnibus()
            return make_response(200, result)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)

    @onibusBP.route("/onibus/<id>",methods=["GET"])
    def getOnibusById(id):
        try:
            bll = OnibusBll()

            result = bll.getOnibusById(id)
            return make_response(result, 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)
        
    @onibusBP.route("/onibus/<id>",methods=["PUT"])
    def updateClient(id):
        try:
            data = request.json
            bll = OnibusBll()

            result = bll.updatedById(id, data)
            response = Response(200, "", result)
            return make_response(response.toDict(), 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)
        
    @onibusBP.route("/onibus/<id>",methods=["DELETE"])
    def deleteClient(id):
        try:
            bll = OnibusBll()

            result = bll.deleteById(id)
            response = Response(200, "", result)
            return make_response(response.toDict(), 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(), 400)
