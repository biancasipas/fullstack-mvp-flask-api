from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///database/db.sqlite3"

engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base()

# importa models para registrar no metadata
from model.paciente import Paciente
from model.consulta import Consulta


def init_db():
    Base.metadata.create_all(bind=engine)