from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy.exc import IntegrityError

from model import Session, Paciente, Consulta
from schemas import *
from logger import logger

from flask_cors import CORS

info = Info(title="Sistema de Pacientes", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

paciente_tag = Tag(name="Paciente")
consulta_tag = Tag(name="Consulta")


@app.get("/")
def home():
    return redirect("/openapi")


# 🧑‍⚕️ Criar paciente
@app.post("/paciente", tags=[paciente_tag])
def add_paciente(form: PacienteSchema):
    session = Session()

    paciente = Paciente(
        nome=form.nome,
        idade=form.idade,
        peso=form.peso
    )

    session.add(paciente)
    session.commit()

    return {
        "id": paciente.id,
        "nome": paciente.nome,
        "idade": paciente.idade,
        "peso": paciente.peso
    }, 200


# 🔍 listar pacientes
@app.get("/pacientes", tags=[paciente_tag])
def get_pacientes():
    session = Session()
    pacientes = session.query(Paciente).all()

    return {
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


# 🗑️ deletar paciente
@app.delete("/paciente", tags=[paciente_tag])
def del_paciente(query: PacienteBuscaSchema):
    session = Session()

    count = session.query(Paciente).filter(Paciente.nome == query.nome).delete()
    session.commit()

    if count:
        return {"message": "Paciente removido"}, 200

    return {"message": "Paciente não encontrado"}, 404


# 🩺 adicionar consulta
@app.post("/consulta", tags=[consulta_tag])
def add_consulta(form: ConsultaSchema):
    session = Session()

    paciente = session.query(Paciente).filter(Paciente.id == form.paciente_id).first()

    if not paciente:
        return {"message": "Paciente não encontrado"}, 404

    consulta = Consulta(form.observacao)

    paciente.adiciona_consulta(consulta)
    session.commit()

    return {
        "paciente": paciente.nome,
        "observacao": form.observacao
    }, 200