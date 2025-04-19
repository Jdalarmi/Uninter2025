from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, index=True)
    status = Column(String)
    observacoes = Column(String, nullable=True)
    
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    medico_id = Column(Integer, ForeignKey("medicos.id"))
    
    paciente = relationship("Paciente", back_populates="consultas")
    medico = relationship("Medico", back_populates="consultas") 