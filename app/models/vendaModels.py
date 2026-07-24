from app.models.defaultModels import TableDefault
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey,UUID
from sqlalchemy.orm import relationship
from datetime import datetime

class VendaModel(TableDefault):
    __tablename__ = "vendas"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    excursao_id = Column(UUID(as_uuid=True), ForeignKey("excursao.id"), nullable=False)
    cliente_titular_id = Column(UUID(as_uuid=True), ForeignKey("clientes.id"), nullable=False) # O pagador
    
    valor_total = Column(Float, nullable=False)
    status_pagamento = Column(String(20), default="PENDENTE") # PENDENTE, PAGO, CANCELADO
    data_venda = Column(DateTime, default=datetime.now())

    titular = relationship("ClienteModel")
    excursao = relationship("Excursaomodel", back_populates="vendas")
    reservas = relationship("ReservaModel", back_populates="venda", cascade="all, delete-orphan")

    def toDict(self):
        return {
            "id": str(self.id),
            "excursao_id": str(self.excursao_id),
            "cliente_titular_id": str(self.cliente_titular_id),
            "valor_total": self.valor_total,
            "status_pagamento": self.status_pagamento,
            "data_venda": self.data_venda.isoformat() if self.data_venda else None
        }