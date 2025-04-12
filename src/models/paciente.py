from sqlalchemy import Column, Integer, String, Date
from ..database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    data_nascimento = Column(Date)
    telefone = Column(String)
    email = Column(String, unique=True, index=True)
    endereco = Column(String) 