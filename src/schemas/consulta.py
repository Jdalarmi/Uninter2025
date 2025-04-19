from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ConsultaBase(BaseModel):
    data_hora: datetime
    status: str
    observacoes: Optional[str] = None
    paciente_id: int
    medico_id: int

class ConsultaCreate(ConsultaBase):
    pass

class Consulta(ConsultaBase):
    id: int

    class Config:
        from_attributes = True 