from pydantic import BaseModel
from datetime import date
from typing import Optional

class PacienteBase(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    telefone: str
    email: str
    endereco: str

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id: int

    class Config:
        orm_mode = True 