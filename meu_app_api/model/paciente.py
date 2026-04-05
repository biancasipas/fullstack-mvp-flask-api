from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from model import Base


class Paciente(Base):
    __tablename__ = "paciente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    # relacionamento com consultas
    consultas = relationship("Consulta", back_populates="paciente_obj", cascade="all, delete-orphan")

    # método auxiliar
    def adiciona_consulta(self, consulta):
        self.consultas.append(consulta)

    def __repr__(self):
        return f"<Paciente {self.nome}>"