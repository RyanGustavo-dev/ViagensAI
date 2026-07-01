import uuid
from app.extension import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from app.models.defaultModels import TableDefault

class OnibusModel(TableDefault):
    __tablename__ = "onibus"

    modelo = db.Column(db.String(), nullable=False)
    marca = db.Column(db.String())
    capacidade = db.Column(db.Integer())
    activo = db.Column(db.Boolean(), default=True)
    