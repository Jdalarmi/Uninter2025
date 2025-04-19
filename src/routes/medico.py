from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database.database import get_db
from models.medico import Medico
from schemas.medico import MedicoCreate, Medico as MedicoSchema
from auth.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=MedicoSchema)
def create_medico(medico: MedicoCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_medico = Medico(**medico.model_dump())
    db.add(db_medico)
    db.commit()
    db.refresh(db_medico)
    return db_medico

@router.get("/", response_model=List[MedicoSchema])
def read_medicos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    medicos = db.query(Medico).offset(skip).limit(limit).all()
    return medicos

@router.get("/{medico_id}", response_model=MedicoSchema)
def read_medico(medico_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    medico = db.query(Medico).filter(Medico.id == medico_id).first()
    if medico is None:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    return medico 