from app.extension import db
from app.models.clientesModels import ClienteModel

class clienteBLL:

    def createNewCliente(self, data):
        cpf = str(data.get("cpf", "")).strip()
        nome = str(data.get("nome","")).strip()

        if not cpf or not nome:
            raise Exception("CPF e Nome são obrigatorios")
        
        cpfExist = db.session.query(ClienteModel).filter(ClienteModel.cpf==cpf).first()
        if cpfExist:
            raise Exception(f"Esse cliente ja está cadastrado: cpf {cpfExist}")

        newCliente = ClienteModel(
            nome=nome,
            cpf=cpf,
            telefone=data.get("telefone"),
            email=data.get("email"),
            titular_id=data.get("titular_id", ""),
            endereco_id=data.get("endereco_id")
        )

        db.session.add(newCliente)
        db.session.commit()

        return {"id ":newCliente.id, "message": "Cliente cadastrado com sucesso!"}
    
    def getClientByCpfOrNome(self, nome, cpf):
        clientByName = db.session.query(ClienteModel).filter(ClienteModel.nome.ilike(f"%{nome}%")).all()
        if clientByName:
            return [client.toDict() for client in clientByName]
        
        clientByCpf = db.session.query(ClienteModel).filter(ClienteModel.cpf.ilike(f"%{cpf}")).all()
        if clientByCpf:
            return [client.toDict() for client in clientByCpf]

        allClients = db.session.query(ClienteModel).all()
        return [client.toDict() for client in allClients]
    
    def updateClient(self, id, data):
        client = db.session.query(ClienteModel).filter(ClienteModel.id==id).first()
        if not client:
            raise Exception("Cliente não encontrado")
        
        client.nome = data.get("nome", client.nome)
        client.cpf = data.get("cpf", client.cpf)
        client.telefone = data.get("telefone", client.telefone)
        client.email = data.get("email", client.email)
        client.titular_id = data.get("titular_id", client.titular_id)
        client.endereco_id = data.get("endereco_id", client.endereco_id)

        db.session.commit()

        return {"id": str(client.id), "message": "Cliente atualizado com sucesso!"}
    
    def deleteClient(self, id):
        client = db.session.query(ClienteModel).filter(ClienteModel.id==id).first()
        if not client:
            raise Exception("Cliente não encontrado")
        
        db.session.delete(client)
        db.session.commit()

        return {"id": str(client.id), "message": "Cliente deletado com sucesso!"}