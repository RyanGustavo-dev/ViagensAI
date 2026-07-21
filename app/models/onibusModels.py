from app.models.defaultModels import TableDefault
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class OnibusModel(TableDefault):
    __tablename__ = "onibus"

    descricao = Column(String, nullable=False)
    capacidade_assento = Column(Integer, nullable=True)

    excursoes = relationship("ExcursaoModel", back_populates="onibus")

    def toDict(self):
        return {
            "id": self.id,
            "descrição": self.descricao,
            "capacidade_assento": self.capacidade_assento
        }