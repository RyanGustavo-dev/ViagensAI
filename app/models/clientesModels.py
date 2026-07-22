from app.models.defaultModels import TableDefault
from sqlalchemy import Column, String, ForeignKey, Integer,UUID, Boolean
from sqlalchemy.orm import relationship

class ClienteModel(TableDefault):
    __tablename__ = "clientes"

    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=True)
    email = Column(String, nullable=True)

    titular_id = Column(UUID(as_uuid=True), ForeignKey("clientes.id"), nullable=True)

    endereco_id = Column(UUID(as_uuid=True), ForeignKey("enderecos.id"), nullable=True)
    endereco = relationship("EnderecoModel")
    acompanhantes = relationship("ClienteModel")

    def toDict(self):
        return {
            "id": str(self.id),
            "nome": self.nome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "email": self.email,
            "titular_id": str(self.titular_id) if self.titular_id else None,
            "endereco_id": str(self.endereco_id) if self.endereco_id else None
        }