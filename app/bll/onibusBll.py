from app.extension import db
from app.models.onibusModels import OnibusModel
from datetime import datetime

class OnibusBll:
    
    def createNewOnibus(self, data):
        newOnibus = OnibusModel(
            descricao = data.get("descricao"),
            capacidade_assento = data.get("capacidade_assento")
        )

        db.session.add(newOnibus)
        db.session.commit()

        return {"id ":newOnibus.id, "message": "Ônibus cadastrado com sucesso!"}
    
    def getAllOnibus(self):
        onibus = db.session.query(OnibusModel).all()
        return [oni.toDict() for oni in onibus]
    
    def getOnibusById(self, id):
        onibus = db.session.query(OnibusModel).filter(OnibusModel.id == id).first()
        return onibus.toDict()
    
    def updatedById(self, id, data):
        oldOnibus = db.session.query(OnibusModel).filter(OnibusModel.id == id).first()

        oldOnibus.descricao = data.get("descricao", oldOnibus.descricao)
        oldOnibus.capacidade_assento = data.get("capacidade_assento", oldOnibus.capacidade_assento)
        oldOnibus.updated_at(datetime)

        db.session.commit()

        return oldOnibus.toDict()
    
    def deleteById(self, id):
        onibus = db.session.query(OnibusModel).filter(OnibusModel.id == id).first()

        db.session.delete(onibus)
        db.session.commit()

        return {"id ":onibus.id, "message": "Ônibus deletado com sucesso!"}