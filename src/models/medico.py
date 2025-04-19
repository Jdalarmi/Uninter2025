from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database.database import Base

class Medico(Base):
    __tablename__ = "medicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    crm = Column(String, unique=True, index=True)
    especialidade = Column(String)
    telefone = Column(String)
    email = Column(String, unique=True, index=True)
    data_admissao = Column(Date)

    consultas = relationship("Consulta", back_populates="medico")