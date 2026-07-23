from app.extension import db
from app.models.vendaModels import VendaModel
from app.models.reservaModels import ReservaModel
from app.models.excursaoModels import Excursaomodel
from app.models.clientesModels import ClienteModel
from sqlalchemy import or_
from datetime import datetime

class VendaBLL:

    def createNewVenda(data):
        excursao_id = data.get("excursao_id")
        cliente_titular_id = data.get("cliente_titular_id")
        # Formato ideal vindo do front: [{"passageiro_id": 1, "assento": 12}, {"passageiro_id": 2, "assento": 13}]
        passageiro_assentos = data.get("passageiro_assentos", [])

        newVenda = VendaModel(
            excursao_id = excursao_id,
            cliente_titular_id = cliente_titular_id,
            valor_total = data.get("valor_total")
        )
        db.session.add(newVenda)
        db.session.flush()

        assentos_desejado = [p["assento"]for p in passageiro_assentos] 

        ocupados = (
            db.session.query(ReservaModel.numero_assento)
            .join(VendaModel)
            .filter(VendaModel.excursao_id == excursao_id)
            .filter(ReservaModel.numero_assento.in_(assentos_desejado))
        )

        if ocupados:
            lista_ocupados = [o[0]for o in ocupados]
            raise Exception (f"As poltronas {', '.join(lista_ocupados)} estão ocupadas no momento")
        

        ids_passageiros = [p["passageiro_id"] for p in passageiro_assentos]
        clientes = (
            db.session.query(ClienteModel)
            .filter(or_(ClienteModel.id == ids_passageiros, ClienteModel.titular_id == cliente_titular_id))
            .filter(ClienteModel.id.in_(ids_passageiros))
            .all()
        )
        if len(clientes) != len(passageiro_assentos):
            raise Exception("Existem passageiros na lista que não estão vinculados a este titular!")

        for pal in passageiro_assentos:
            newRerva = ReservaModel(
                venda_id = newVenda.id,
                passageiro_id = pal["passageiro_id"],
                numero_assento = pal["assento"]
            )
            db.session.add(newRerva)

        db.session.commit()

        return {"id ": str(newVenda.id), "message": "Venda realizada com sucesso!"}

    def getVendasForExcursaoOrClienteOrId(self, excursao_id=None, cliente_id=None, venda_id=None):

        vendaForExcursao = db.session.query(VendaModel).filter(VendaModel.excursao_id == excursao_id).all()
        if vendaForExcursao:
            return [venda.toDict() for venda in vendaForExcursao]

        vendaForCliente = db.session.query(VendaModel).filter(VendaModel.cliente_titular_id == cliente_id).all()
        if vendaForCliente:
            return [venda.toDict() for venda in vendaForCliente]

        vendaForId = db.session.query(VendaModel).filter(VendaModel.id == venda_id).first()
        if vendaForId:
            return vendaForId.toDict()

        reservas = db.session.query(VendaModel).all()
        return [reserva.toDict() for reserva in reservas]

    def getVendaById(self, venda_id):

        vendaResult = db.session.query(VendaModel).filter(VendaModel.id == venda_id).first()
        if not vendaResult:
            raise Exception ("Venda não encontrada!")

        excursaoResult = db.session.query(Excursaomodel).filter(Excursaomodel.id == str(vendaResult.excursao_id)).first()
        titulaResult = db.session.query(ClienteModel).filter(ClienteModel.id == str(vendaResult.cliente_titular_id)).first()

        reservas = (
            db.session.query(ReservaModel.id, ReservaModel.numero_assento, ClienteModel)
            .join(ClienteModel, ClienteModel.id == ReservaModel.passageiro_id)
            .filter(ReservaModel.venda_id == venda_id)
            .all()
        )

        listaPassageiro = []
        for reserva_id, assento, cliente in reservas:
            listaPassageiro.append(
                {
                    "reserva_id": str(reserva_id),
                    "passageiro_id": str(cliente.id),
                    "nome":str(cliente.nome),
                    "assento": assento
                }
            )

        return {
            "id": str(vendaResult.id),
            "data_venda": str(vendaResult.created_at),
            "valor_total": vendaResult.valor_total,
            "status_pagamento": vendaResult.status_pagamento,
            "excursao": {
                "id": excursaoResult.id,
                "titulo": excursaoResult.titulo,
                "data_saida": excursaoResult.data_saida
            },
            "titular": {
                "id": titulaResult.id,
                "nome": titulaResult.nome,
                "cpf": titulaResult.cpf,
                "telefone": titulaResult.telefone
            },
            "passageiro": listaPassageiro
        }
    
    def alterarStatusPagamento(self, venda_id, novo_status):
        venda = db.session.query(VendaModel).filter(VendaModel.id == venda_id).first()
        if not venda:
            raise Exception("Venda não encontrada!")

        venda.status_pagamento = novo_status
        venda.updated_at = datetime.now()

        db.session.commit()

        return {"id": str(venda.id), "message": "Status de pagamento atualizado com sucesso!"}