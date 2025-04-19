from pydantic import BaseModel
from datetime import date
from typing import Optional

class MedicoBase(BaseModel):
    nome: str
    crm: str
    especialidade: str
    telefone: str
    email: str
    data_admissao: date

class MedicoCreate(MedicoBase):
    pass

class Medico(MedicoBase):
    id: int

    class Config:
        from_attributes = True 