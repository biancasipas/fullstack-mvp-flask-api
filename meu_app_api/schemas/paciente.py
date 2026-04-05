from pydantic import BaseModel
from typing import Optional, List


class PacienteSchema(BaseModel):
    nome: str
    idade: int
    peso: float


class PacienteBuscaSchema(BaseModel):
    nome: Optional[str] = None
    limit: int = 10
    skip: int = 0


class ConsultaSchema(BaseModel):
    paciente_id: int
    observacao: str


class PacienteViewSchema(BaseModel):
    id: int
    nome: str
    idade: int
    peso: float
    total_consultas: int
    consultas: List[dict]