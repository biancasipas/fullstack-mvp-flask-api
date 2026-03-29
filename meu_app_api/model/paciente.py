from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model.base import Base


class Paciente(Base):
    __tablename__ = "paciente"

    id = Column(Integer, primary_key=True)
    nome = Column(String(140), nullable=False)
    idade = Column(Integer)
    peso = Column(Float)
    data_cadastro = Column(DateTime, default=datetime.now)

    consultas = relationship(
        "Consulta",
        back_populates="paciente_obj",
        cascade="all, delete-orphan"
    )

    def __init__(self, nome: str, idade: int, peso: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def adiciona_consulta(self, consulta):
        self.consultas.append(consulta)