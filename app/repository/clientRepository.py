from uuid import uuid4
from datetime import datetime
from app.extension import db
from app.models.clienteModel import ClientModel

class ClientRepository:

    def get_all(self):
        return ClientModel.query.filter_by(ClientModel.deleted_at != None).all()
    
    def get_by_id(self, client_id:uuid4):
        return ClientModel.query.get(client_id).filter_by(ClientModel.deleted_at != None).first()
    
    def get_by_email(self, email: str):
        return ClientModel.query.filter_by(email=email).first()

    def create_client(self, data: dict) -> ClientModel:
        client = ClientModel(**data)
        db.session.add(client)
        db.session.commit()
        return client
    
    def updated_client(self, client:ClientModel, data:dict) -> ClientModel:

        for key, value in data.items():
            setattr(client, key, value)
        db.session.commit()
        return client
    
    def delete_clint( self, client: ClientModel) -> None:
        client.deleted_at=datetime.now
        db.session.commit()

client_repository = ClientRepository()