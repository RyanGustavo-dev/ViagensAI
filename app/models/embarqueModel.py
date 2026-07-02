import uuid
from app.extension import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from app.models.defaultModels import TableDefault

embarque_excursao = db.Table(
    "embarque_excursao",
    db.Column("excursao_id", UUID(as_uuid=True), db.ForeignKey("excursao.id")),
    db.Column("embarque_id", UUID(as_uuid=True), db.ForeignKey("embarque.id"))
)

class EmbarqueModel(TableDefault):
    __tablename__ = 'embarque'

    local_embarque = db.Column(db.String(200))
    horario_embarque = db.Column(db.String(20))

    excursoes = db.relationship(
        "ExcursaoModel",
        secondary='embarque_excursao',
        back_populates="embarques"
    )