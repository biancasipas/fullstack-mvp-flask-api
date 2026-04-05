from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///db.sqlite3"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

from model.base import Base
from model.paciente import Paciente
from model.consulta import Consulta

# cria as tabelas
Base.metadata.create_all(engine)