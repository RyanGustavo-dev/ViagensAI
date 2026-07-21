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