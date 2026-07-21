from app.extension import db
from app.models.enderecoModels import EnderecoModel
from datetime import datetime

class EnderecoBLL:

    def createNewEndereco(self, data):
        newClient = EnderecoModel(
            cep=data.get("cep"),
            logradouro=data.get("logradouro"),
            numero=data.get("numero"),
            complemento=data.get("complemento"),
            bairro=data.get("bairro"),
            cidade=data.get("cidade"),
            estado=data.get("estado")
        )
        db.session.add(newClient)
        db.session.commit()

        return {"message": "Endereco criado com sucesso!"}
    
    def getAllEnderecos(self):
        endereco = db.session.query(EnderecoModel).all()
        return [end.toDict() for end in endereco]

    def getByID(self,id):
        return db.session.query(EnderecoModel).filter(EnderecoModel.id == id).first()
    
    def editEndereco(self, id, data):
        oldEndereco = self.getByID(id)

        if not oldEndereco:
            return {"message": "Endereço não foi encontrado!"}
        
        if data.get("cep"):
            oldEndereco.cep = data.get("cep")
        if data.get("logradouro"):
            oldEndereco.logradouro = data.get("logradouro")
        if data.get("numero"):
            oldEndereco.numero = data.get("numero")
        if data.get("complemento"):
            oldEndereco.complemento = data.get("complemento")
        if data.get("bairro"):
            oldEndereco.bairro = data.get("bairro")
        if data.get("cidade"):
            oldEndereco.cidade = data.get("cidade")
        if data.get("estado"):
            oldEndereco.estado = data.get("estado")

        oldEndereco.updated_at(datetime.now)
        
        db.session.commit()
    
    def getEnderecoById(self, id):
        endereco = self.getByID(id)

        if not endereco:
            return {"message": "Endereço não foi encontrado!"}
        
        return endereco.toDict()
    
    def deleteEndereco(self, id):
        endereco = self.getByID(id)

        db.session.delete(endereco)
        db.session.commit()

        return {"message": "Usuário deletado com sucesso!"}