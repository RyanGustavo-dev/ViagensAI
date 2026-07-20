from app.models.defaultModels import TableDefault
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class OnibusModel(TableDefault):
    __tablename__ = "onbius"

    descricao = Column(String, nullable=False)
    capacidade_assento = Column(Integer, nullable=True)

    excursoes = relationship("ExcursaoModel", back_populates="onibus")