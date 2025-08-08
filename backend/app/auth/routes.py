# Importações principais do FastAPI
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

# Importações internas da aplicação
from app.models import schemas  # Schemas Pydantic usados para validação e resposta
from app.auth import crud, security  # CRUD de utilizadores e funções de segurança (hash, JWT)
from app.database import database  # Função para obter sessão da BD

# Criação do router com prefixo e tag para organização na documentação da API
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# Endpoint de Login
# Recebe email e password no formato OAuth2 (username = email), valida e retorna token JWT
@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(database.get_db)
):
    # Autentica o utilizador (valida email e password)
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    
    if not user:
        # Erro se credenciais estiverem erradas
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        # Erro se o utilizador estiver inativo
        raise HTTPException(status_code=400, detail="Utilizador inativo")

    # Define tempo de expiração do token
    access_token_expires = timedelta(minutes=60)

    # Cria o token JWT
    access_token = security.create_access_token(
        data={"sub": user.email}, 
        expires_delta=access_token_expires
    )

    # Retorna o token de acesso e tipo
    return {"access_token": access_token, "token_type": "bearer"}