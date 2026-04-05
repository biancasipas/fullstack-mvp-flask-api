from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from model.base import Base


class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    consultas = relationship(
        "Consulta",
        back_populates="paciente",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Paciente(nome={self.nome}, idade={self.idade})>"