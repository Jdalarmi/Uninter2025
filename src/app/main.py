from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from .database import engine, Base
from .routes import paciente
from .auth.jwt_handler import create_access_token
from .auth.dependencies import get_current_user
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(
    paciente.router,
    prefix="/pacientes",
    tags=["pacientes"]
)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # This is a simplified login. In a real application, you should verify
    # the user credentials against the database
    if form_data.username != "admin@example.com" or form_data.password != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao SGHSS"} 