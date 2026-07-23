from app.bll.vendasBll import VendaBLL
from app.models.responseModels import Response
from flask import make_response, request, Blueprint

reservaBP = Blueprint("reserva",__name__)

class reservaController:
    
    @reservaBP.route("/vendas", methods=["POST"])
    def createNewVenda():
        try:
            data = request.json
            bll = VendaBLL()

            resultado = bll.createNewVenda(data)

            response = Response(200, "", resultado)
            return make_response(response.toDict(), 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(),400)
    
    @reservaBP.route("/vendas", methods=["GET"])
    def getVendas():
        try:
            excursao_id = request.args.get("excursao_id")
            cliente_id = request.args.get("cliente_id")
            venda_id = request.args.get("venda_id")
            bll = VendaBLL()

            resultado = bll.getVendasForExcursaoOrClienteOrId(excursao_id, cliente_id, venda_id)
            return make_response(resultado, 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(),400)

    @reservaBP.route("/vendas/<id>", methods=["GET"])
    def getVendaById(id):
        try:
            bll = VendaBLL()

            resultado = bll.getVendaById(id)
            return make_response(resultado, 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(),400)

    @reservaBP.route("/vendas/<id>/pagamento", methods=["PATCH"])
    def updateVendaStatus(id):
        try:
            data = request.json

            bll = VendaBLL()

            resultado = bll.alterarStatusPagamento(id, data.get("status"))
            response = Response(200, "", resultado)
            return make_response(response.toDict(), 200)
        
        except Exception as e:
            response = Response(400, str(e), {})
            return make_response(response.toDict(),400)