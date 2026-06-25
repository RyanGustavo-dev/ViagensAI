import uuid
from app.extension import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from app.models.defaultModels import TableDefault

class ClientModel(TableDefault):
    __tablename__ = "clients"

    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    rg = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    logradouro = db.Column(db.String)
    numero = db.Column(db.String)
    bairro = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)
    cep = db.Column(db.String)
    data_nascimento = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Client {self.email}"