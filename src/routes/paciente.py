from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database.database import get_db
from models import paciente as models
from schemas import paciente as schemas
from auth.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Paciente)
def create_paciente(
    paciente: schemas.PacienteCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_paciente = models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@router.get("/{paciente_id}", response_model=schemas.Paciente)
def read_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_paciente = db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return db_paciente

@router.get("/", response_model=List[schemas.Paciente])
def read_pacientes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    pacientes = db.query(models.Paciente).offset(skip).limit(limit).all()
    return pacientes

@router.put("/{paciente_id}", response_model=schemas.Paciente)
def update_paciente(
    paciente_id: int,
    paciente: schemas.PacienteCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_paciente = db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    
    for key, value in paciente.dict().items():
        setattr(db_paciente, key, value)
    
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@router.delete("/{paciente_id}")
def delete_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    db_paciente = db.query(models.Paciente).filter(models.Paciente.id == paciente_id).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    
    db.delete(db_paciente)
    db.commit()
    return {"message": "Paciente deletado com sucesso"} 