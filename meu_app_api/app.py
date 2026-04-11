import os

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, send_from_directory
from flask_cors import CORS
from contextlib import contextmanager

from model.base import Session as DBSession, engine, Base
from model.paciente import Paciente
from model.consulta import Consulta

from schemas.paciente import PacienteSchema, PacientePathSchema
from schemas.paciente import ConsultaSchema 

from logger import logger

Base.metadata.create_all(engine)

info = Info(title="Sistema Clínico MVP", version="1.0")
app = OpenAPI(__name__, info=info)
CORS(app)

paciente_tag = Tag(name="Paciente")
consulta_tag = Tag(name="Consulta")

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

# ==================== CRIAR PACIENTE (SWAGGER) ====================
@app.post("/paciente", tags=[paciente_tag])
def criar_paciente(form: PacienteSchema):

    with get_db() as session:

        paciente_existente = session.query(Paciente)\
            .filter(Paciente.nome.ilike(form.nome.strip()))\
            .first()

        if paciente_existente:
            return {"erro": "Paciente já cadastrado com esse nome"}, 400

        paciente = Paciente(
            nome=form.nome.strip(),
            idade=form.idade,
            peso=form.peso
        )

        session.add(paciente)
        session.flush()

        return {
            "sucesso": True,
            "id": paciente.id,
            "nome": paciente.nome,
            "idade": paciente.idade,
            "peso": paciente.peso
        }, 201

# ==================== CRIAR PACIENTE (HTML / JSON) ====================
@app.post("/paciente_json", tags=[paciente_tag])
def criar_paciente_json():

    data = request.get_json()

    if not data:
        return {"erro": "JSON inválido"}, 400

    nome = data["nome"].strip()

    with get_db() as session:

        paciente_existente = session.query(Paciente)\
            .filter(Paciente.nome.ilike(nome))\
            .first()

        if paciente_existente:
            return {"erro": "Paciente já cadastrado com esse nome"}, 400

        paciente = Paciente(
            nome=nome,
            idade=int(data["idade"]),
            peso=float(data["peso"])
        )

        session.add(paciente)
        session.flush()

        return {
            "sucesso": True,
            "mensagem": "Paciente criado com sucesso"
        }, 201

# ==================== LISTAR PACIENTES ====================
@app.get("/paciente", tags=[paciente_tag])
def listar_pacientes(nome: str = None):

    with get_db() as session:

        query = session.query(Paciente)

        if nome:
            query = query.filter(Paciente.nome.ilike(f"%{nome}%"))

        pacientes = query.all()

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

# ==================== DELETAR PACIENTE ====================
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

# ==================== CRIAR CONSULTA ====================
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
        session.flush()

        logger.info("Consulta criada")

        return {"sucesso": True}, 201
    
# ==================== FRONTEND ====================

@app.get("/app")
def frontend():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    front_dir = os.path.abspath(
        os.path.join(base_dir, "..", "meu_app_front", "meu_app_front")
    )

    return send_from_directory(front_dir, "index.html")

# ==================== RUN ====================
if __name__ == "__main__":
    app.run(debug=True, port=5000)