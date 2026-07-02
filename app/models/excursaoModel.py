import enum
import uuid
from app.extension import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from app.models.defaultModels import TableDefault

class StatusViagem(str, enum.Enum):
    CONCLUIDA="CONCLUIDA",
    EM_ANDAMENTO="ANDAMENTO",
    CANCELADA="CANCELADA"
    

class ExcursaoModel(TableDefault):
    __tablename__ = "excursao"

    hotel = db.Column(db.String())
    origem = db.Column(db.String())
    destino = db.Column(db.String())
    data_saida= db.Column(db.Date())
    data_retorno = db.Column(db.Date())
    status_viagem = db.Column(db.Enum(StatusViagem), default=StatusViagem.EM_ANDAMENTO)

    embarques = db.relationship(
        "EmbarqueModel",
        secondary="embarque_excursao",
        back_populates="excursoes"
    )

