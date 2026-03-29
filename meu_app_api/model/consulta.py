from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model.base import Base


class Consulta(Base):
    __tablename__ = "consulta"

    id = Column(Integer, primary_key=True)
    observacao = Column(String(4000))
    data = Column(DateTime, default=datetime.now)

    paciente_id = Column(
        Integer,
        ForeignKey("paciente.id"),
        nullable=False
    )

    paciente_obj = relationship(
        "Paciente",
        back_populates="consultas"
    )

    def __init__(self, observacao: str):
        self.observacao = observacao