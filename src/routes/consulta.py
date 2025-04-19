from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database.database import get_db
from models.consulta import Consulta
from models.paciente import Paciente
from models.medico import Medico
from schemas.consulta import ConsultaCreate, Consulta as ConsultaSchema
from auth.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=ConsultaSchema)
def create_consulta(consulta: ConsultaCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    paciente = db.query(Paciente).filter(Paciente.id == consulta.paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    
    medico = db.query(Medico).filter(Medico.id == consulta.medico_id).first()
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    
    db_consulta = Consulta(**consulta.model_dump())
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta

@router.get("/", response_model=List[ConsultaSchema])
def read_consultas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    consultas = db.query(Consulta).offset(skip).limit(limit).all()
    return consultas

@router.get("/paciente/{paciente_id}", response_model=List[ConsultaSchema])
def read_consultas_by_paciente(paciente_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    consultas = db.query(Consulta).filter(Consulta.paciente_id == paciente_id).all()
    if not consultas:
        raise HTTPException(status_code=404, detail="Nenhuma consulta encontrada para este paciente")
    return consultas

@router.get("/medico/{medico_id}", response_model=List[ConsultaSchema])
def read_consultas_by_medico(medico_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    consultas = db.query(Consulta).filter(Consulta.medico_id == medico_id).all()
    if not consultas:
        raise HTTPException(status_code=404, detail="Nenhuma consulta encontrada para este médico")
    return consultas 