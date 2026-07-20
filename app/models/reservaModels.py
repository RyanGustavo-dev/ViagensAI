from app.models.defaultModels import TableDefault
from sqlalchemy import Column, String, Integer, ForeignKey,UUID
from sqlalchemy.orm import relationship


class ReservaModel(TableDefault):
    __tablename__ = "reservas"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    venda_id = Column(UUID(as_uuid=True), ForeignKey("vendas.id"), nullable=False)
    passageiro_id = Column(UUID(as_uuid=True), ForeignKey("clientes.id"), nullable=False)
    
    numero_assento = Column(Integer, nullable=False)

    venda = relationship("VendaModel", back_populates="reservas")
    passageiro = relationship("ClienteModel")