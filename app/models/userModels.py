from app.models.defaultModels import TableDefault
from sqlalchemy import Column, String, ForeignKey, Integer, UUID
from sqlalchemy.orm import relationship

class UserModels(TableDefault):
    __tablename__ = "users"

    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=True)
    email = Column(String, nullable=True)

    endereco_id = Column(UUID(as_uuid=True), ForeignKey("enderecos.id"), nullable=True)
    endereco = relationship("EnderecoModels")
    