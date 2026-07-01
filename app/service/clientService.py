from app.repository.clientRepository import client_repository
from app.utils.extensions import ConflictError, NotFoundException

class UserService:

    def create_cliente(self, data):
        exist = client_repository.get_by_email(data["email"])
        if exist:
            return ConflictError("Já existe cliente com esse nome")
        
        return client_repository.create_client(data)

    def get_all_clients(self):
        return client_repository.get_all()
    
    def get_client_by_id(self, id):
        return client_repository.get_by_id(id)
    
    def delete_client(self, id):
        client = client_repository.get_by_id(id)
        if not client:
            return NotFoundException("Cliente não encontrado!")
        return client_repository.delete_clint(client)
    
    def update_client(self, id, data):
        client = client_repository.get_by_id(id)
        if not client:
            return NotFoundException("Cliente não encontrado!")
        
        new = client_repository.get_by_email(data["email"])
        if new and new.id != id:
            return ConflictError(f"Ja existe um cliente com esse email {data["email"]}")
        
        return client_repository.updated_client(new, data)
        

