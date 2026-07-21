from app.models.defaultModels import TableDefault
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey,UUID
from sqlalchemy.orm import relationship

class Excursaomodel(TableDefault):
    __tablename__ = "excursao"

    codigo = Column(String, unique=True, nullable=False)
    titulo = Column(String, nullable=False)
    hotel = Column(String, nullable=True)
    valor_por_pessoa = Column(Float, nullable=False)
    data_saida = Column(DateTime, nullable=False)
    data_retorno = Column(DateTime, nullable=False)

    destino_id = Column(UUID(as_uuid=True), ForeignKey("enderecos.id"), nullable=False)
    onibus_id = Column(UUID(as_uuid=True), ForeignKey("onibus.id"), nullable=False)

    destino = relationship("EnderecoModel")
    onibus = relationship("OnibusModel", back_populates="excursao")
    vendas = relationship("VendaModel", back_populates="excursao")