from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS
from contextlib import contextmanager

from model import Session as DBSession, Paciente, Consulta
from model.base import Base
from model import engine

from schemas.paciente import PacienteSchema, PacientePathSchema
from schemas.consulta import ConsultaSchema

from logger import logger

# ==================== DB INIT ====================
Base.metadata.create_all(engine)

# ==================== APP ====================
info = Info(title="Sistema Clínico MVP", version="1.0")
app = OpenAPI(__name__, info=info)
CORS(app)

paciente_tag = Tag(name="Paciente")
consulta_tag = Tag(name="Consulta")

# ==================== DB SESSION ====================
@contextmanager
def get_db():
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# ==================== HOME ====================
@app.get("/")
def home():
    return redirect("/openapi")

# ========================= GET =============================

@app.get("/paciente/<int:paciente_id>", tags=[paciente_tag])
def buscar_paciente(path: PacientePathSchema):

    with get_db() as session:

        paciente = session.query(Paciente).filter_by(id=path.paciente_id).first()

        if not paciente:
            return {"erro": "Paciente não encontrado"}, 404

        return {
            "id": paciente.id,
            "nome": paciente.nome,
            "idade": paciente.idade,
            "peso": paciente.peso,
            "consultas": [
                {
                    "id": c.id,
                    "observacao": c.observacao
                }
                for c in paciente.consultas
            ]
        }, 200

# ==================== CREATE PACIENTE ====================
@app.post("/paciente", tags=[paciente_tag])
def criar_paciente(form: PacienteSchema):

    with get_db() as session:
        paciente = Paciente(
            nome=form.nome.strip(),
            idade=form.idade,
            peso=form.peso
        )

        session.add(paciente)

        return {
            "sucesso": True,
            "id": paciente.id,
            "nome": paciente.nome,
            "idade": paciente.idade,
            "peso": paciente.peso
        }, 201

# ==================== LIST PACIENTES ====================
@app.get("/paciente", tags=[paciente_tag])
def listar_pacientes():

    with get_db() as session:
        pacientes = session.query(Paciente).all()

        return {
            "sucesso": True,
            "total": len(pacientes),
            "pacientes": [
                {
                    "id": p.id,
                    "nome": p.nome,
                    "idade": p.idade,
                    "peso": p.peso
                }
                for p in pacientes
            ]
        }, 200

# ==================== DELETE PACIENTE ====================
@app.delete("/paciente/<int:paciente_id>", tags=[paciente_tag])
def deletar_paciente(path: PacientePathSchema):

    with get_db() as session:

        paciente = session.query(Paciente).filter_by(id=path.paciente_id).first()

        if not paciente:
            return {"erro": "Paciente não encontrado"}, 404

        session.delete(paciente)

        return {
            "sucesso": True,
            "mensagem": "Paciente deletado",
            "id": path.paciente_id
        }, 200

# ==================== CREATE CONSULTA ====================
@app.post("/consulta", tags=[consulta_tag])
def criar_consulta(form: ConsultaSchema):

    with get_db() as session:

        paciente = session.query(Paciente).filter_by(id=form.paciente_id).first()

        if not paciente:
            return {"erro": "Paciente não encontrado"}, 404

        consulta = Consulta(
            observacao=form.observacao,
            paciente_id=form.paciente_id
        )

        session.add(consulta)

        logger.info("Consulta criada")

        return {"sucesso": True}, 201

# ==================== HEALTH ====================
@app.get("/health")
def health():
    return {"sucesso": True}, 200

# ==================== RUN ====================
if __name__ == "__main__":
    app.run(debug=True, port=5000)