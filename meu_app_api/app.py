from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import func
from contextlib import contextmanager
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

from model import Session as DBSession, Paciente, Consulta
from schemas import *
from logger import logger

# ==================== SCHEMAS ====================
class ResponseBase(BaseModel):
    sucesso: bool = Field(..., description="Status da operação")

class PacienteResponse(BaseModel):
    sucesso: bool
    id: int
    nome: str
    idade: int
    peso: str
    criado_em: Optional[str] = None

class PacienteListResponse(BaseModel):
    sucesso: bool
    total: int
    pagina: int
    limite: int
    pacientes: List[dict]  # ✅ corrigido

class ErrorResponse(BaseModel):
    erro: str

# ==================== CONFIG ====================
info = Info(title="Sistema Clínico", version="1.0")
app = OpenAPI(__name__, info=info)
CORS(app)

paciente_tag = Tag(name="Paciente")
consulta_tag = Tag(name="Consulta")

# ==================== SESSION ====================
@contextmanager
def get_db_session():
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# ==================== HELPERS ====================
def paciente_duplicado(session: Session, nome: str) -> bool:
    return session.query(Paciente).filter(
        func.lower(Paciente.nome) == func.lower(nome.strip())
    ).first() is not None

def get_paciente(session: Session, paciente_id: int) -> Paciente:
    paciente = session.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise ValueError(f"Paciente ID {paciente_id} não encontrado")
    return paciente

# ==================== ROTAS ====================
@app.get("/")
def home():
    return redirect("/openapi")

# 🧑‍⚕️ Criar paciente
@app.post("/paciente", tags=[paciente_tag])
def add_paciente(form: PacienteSchema):
    with get_db_session() as session:
        if paciente_duplicado(session, form.nome):
            return ErrorResponse(erro=f"Paciente '{form.nome}' já existe"), 409

        if not (0 <= form.idade <= 120):
            return ErrorResponse(erro="Idade inválida"), 400

        paciente = Paciente(
            nome=form.nome.strip().title(),
            idade=form.idade,
            peso=round(form.peso, 2)
        )

        session.add(paciente)
        session.flush()  # ✅ garante ID

        logger.info(f"Paciente criado: {paciente.nome} (ID: {paciente.id})")

        return PacienteResponse(
            sucesso=True,
            id=paciente.id,
            nome=paciente.nome,
            idade=paciente.idade,
            peso=f"{paciente.peso}kg",
            criado_em=datetime.now().isoformat()
        ), 201

# 🔍 Listar pacientes
@app.get("/pacientes", tags=[paciente_tag])
def get_pacientes():
    with get_db_session() as session:
        q = session.query(Paciente)

        if query.nome:
            q = q.filter(func.lower(Paciente.nome).contains(query.nome.lower()))

        total = q.count()
        pacientes = q.limit(query.limit).offset(query.skip).all()

        return PacienteListResponse(
            sucesso=True,
            total=total,
            pagina=(query.skip // query.limit) + 1,
            limite=query.limit,
            pacientes=[
                {
                    "id": p.id,
                    "nome": p.nome,
                    "idade": p.idade,
                    "peso": f"{p.peso}kg"
                } for p in pacientes
            ]
        ), 200

# 🗑️ Deletar paciente
@app.delete("/paciente", tags=[paciente_tag])
def del_paciente(query: PacienteBuscaSchema):
    with get_db_session() as session:
        paciente = session.query(Paciente).filter(
            func.lower(Paciente.nome) == query.nome.lower()
        ).first()

        if not paciente:
            return ErrorResponse(erro="Paciente não encontrado"), 404

        session.delete(paciente)

        logger.info(f"Paciente removido: {paciente.nome}")

        return ResponseBase(sucesso=True), 200

# 🩺 Adicionar consulta
@app.post("/consulta", tags=[consulta_tag])
def add_consulta(form: ConsultaSchema):
    with get_db_session() as session:
        try:
            paciente = get_paciente(session, form.paciente_id)

            if len(form.observacao.strip()) < 5:
                return ErrorResponse(erro="Observação muito curta"), 400

            consulta = Consulta(
                observacao=form.observacao.strip(),
                paciente_id=form.paciente_id
            )

            paciente.adiciona_consulta(consulta)

            logger.info(f"Consulta adicionada para: {paciente.nome}")

            return ResponseBase(sucesso=True), 201

        except ValueError as e:
            return ErrorResponse(erro=str(e)), 404

# ❤️ Health check
@app.get("/health")
def health():
    return ResponseBase(sucesso=True), 200

# ==================== RUN ====================
if __name__ == "__main__":
    app.run(debug=True, port=5000)