from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from model.base import Base


class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    observacao = Column(String(4000), nullable=False)
    data = Column(DateTime, default=datetime.utcnow)

    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)

    paciente = relationship(
        "Paciente",
        back_populates="consultas"
    )

    def __init__(self, observacao: str, paciente_id: int):
        self.observacao = observacao
        self.paciente_id = paciente_id

    def __repr__(self):
        return f"<Consulta(paciente_id={self.paciente_id})>"