from app.models.defaultModels import TableDefault
from sqlalchemy import Column, String

class EnderecoModel(TableDefault):
    __tablename__ =  "enderecos"

    cep = Column(String(), nullable=False)
    logradouro = Column(String, nullable=False)
    numero = Column(String, nullable=False)
    complemento = Column(String, nullable=True)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)