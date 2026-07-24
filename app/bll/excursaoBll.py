from app.extension import db
from app.models.excursaoModels import Excursaomodel
from app.models.vendaModels import VendaModel
from app.models.clientesModels import ClienteModel
from app.models.reservaModels import ReservaModel
from app.models.onibusModels import OnibusModel
from datetime import datetime

class ExcursaoBLL:
    
    def createNewExcusao(data):

        excur = db.session.query(Excursaomodel).filter(Excursaomodel.codigo == data.get("codigo")).first()
        if excur:
            raise Exception(f"O Codigo {data.get('codigo')} já existe!")

        data_saida = data.get("data_saida")
        data_retorno = data.get("data_retorno")

        if isinstance(data_saida, str) and data_saida:
            data_saida = datetime.fromisoformat(data_saida.replace("Z", "+00:00"))
        if isinstance(data_retorno, str) and data_retorno:
            data_retorno = datetime.fromisoformat(data_retorno.replace("Z", "+00:00"))
        
        newExcursao = Excursaomodel(
            codigo = data.get("codigo"),
            titulo = data.get("titulo", ""),
            hotel = data.get("hotel"),
            valor_por_pessoa = data.get("valor_por_pessoa", ""),
            data_saida = data_saida,
            data_retorno = data_retorno, 
            destino_id = data.get("destino_id", ""),
            onibus_id = data.get("onibus_id", "")
        )

        db.session.add(newExcursao)
        db.session.commit()

        return newExcursao.toDict()
    
    def getAllExcursao(self, date_start, date_end, destino_id, codigo):
        query = db.session.query(Excursaomodel)

        if date_start:
            query = query.filter(Excursaomodel.data_saida >= date_start)
        if date_end:
            query = query.filter(Excursaomodel.data_retorno <= date_end)
        if destino_id:
            query = query.filter(Excursaomodel.destino_id == destino_id)
        if codigo:
            query = query.filter(Excursaomodel.codigo.ilike(f"%{codigo}%"))

        excursao = query.all()
        return [exc.toDict() for exc in excursao]

    def getExcursaoById(self, id):
        excursao = db.session.query(Excursaomodel).filter(Excursaomodel.id == id).first()
        if not excursao:
            raise Exception("Excursão não encontrada")
        
        return excursao.toDict()

    def editExcursao(self, id, data):
        excursao = db.session.query(Excursaomodel).filter(Excursaomodel.id == id).first()
        if not excursao:
            raise Exception("Excursão não encontrada")
        
        excursao.codigo = data.get("codigo", excursao.codigo)
        excursao.titulo = data.get("titulo", excursao.titulo)
        excursao.hotel = data.get("hotel", excursao.hotel)
        excursao.valor_por_pessoa = data.get("valor_por_pessoa", excursao.valor_por_pessoa)
        excursao.data_saida = data.get("data_saida", excursao.data_saida)
        excursao.data_retorno = data.get("data_retorno", excursao.data_retorno)
        excursao.destino_id = data.get("destino_id", excursao.destino_id)
        excursao.onibus_id = data.get("onibus_id", excursao.onibus_id)

        db.session.commit()

        return {"id": str(excursao.id), "message": "Excursão atualizada com sucesso!"}
    
    def deleteExcursao(self, id):
        excursao = db.session.query(Excursaomodel).filter(Excursaomodel.id == id).first()
        if not excursao:
            raise Exception("Excursão não encontrada")
        
        db.session.delete(excursao)
        db.session.commit()

        return {"id": str(excursao.id), "message": "Excursão deletada com sucesso!"}

    def getListaPassageiros(self, id):
        excursao = db.session.query(Excursaomodel).filter(Excursaomodel.id == id).first()
        if not excursao:
            raise Exception("Excursão não encontrada")

        resultados = (
            db.session.query(ClienteModel, ReservaModel.numero_assento)
            .join(ReservaModel, ReservaModel.passageiro_id == ClienteModel.id)
            .join(VendaModel, VendaModel.id == ReservaModel.venda_id)
            .filter(VendaModel.excursao_id == id)
            .all()
        )

        listaViagem = []

        for cliente, assento in resultados:
            listaViagem.append({
                "nome":cliente.nome,
                "cpf":cliente.cpf,
                "telefone":cliente.telefone,
                "assento": assento
            })

        return listaViagem
        
    def getListaAssentos(self, id):
        excursao = db.session.query(Excursaomodel).filter(Excursaomodel.id == id).first()
        if not excursao:
            raise Exception("Excursão não encontrada")

        capacidade_atual = excursao.onibus.capacidade_assento

        resultados = (
            db.session.query(ReservaModel.numero_assento)
            .join(VendaModel, VendaModel.id == ReservaModel.venda_id)
            .filter(VendaModel.excursao_id == id)
            .filter(VendaModel.status_pagamento != "CANCELADO")
            .all()
        )

        lista_ouculpados = [assentos[0] for assentos in resultados]
        mapa_onibus =[]

        for numero in range(1, capacidade_atual+1):
            mapa_onibus.append({
                "assento":numero,
                "status":"OUCUPADO" if numero in lista_ouculpados else "LIVRE"
            })

        return mapa_onibus

        

        
