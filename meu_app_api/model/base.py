from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()

db_path = "database/"
os.makedirs(db_path, exist_ok=True)

db_url = f"sqlite:///{db_path}db.sqlite3"

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
