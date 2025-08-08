# Importações principais do FastAPI
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

# Importações de funções auxiliares para segurança e autenticação
from app.auth.utils import (
    hash_password,
    verify_password,
    create_jwt_token,
    generate_totp_secret,
    verify_totp_token
)

# Função para obter utilizador pelo email (da camada de dados)
from app.database import get_user_by_email  # Supondo que esta função exista

# Criação do router para rotas de autenticação com 2FA
auth_router = APIRouter()

# Modelo Pydantic para pedido de login
class LoginRequest(BaseModel):
    email: str
    password: str

# Modelo Pydantic para verificação do segundo fator (TOTP)
class TOTPVerifyRequest(BaseModel):
    email: str
    token: str

# Endpoint de login (primeira etapa)
# Valida email e password. Se corretos, exige verificação TOTP antes de emitir o token JWT.
@auth_router.post("/login")
def login(data: LoginRequest):
    user = get_user_by_email(data.email)
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"message": "TOTP required", "email": user.email}

# Endpoint de verificação do segundo fator (TOTP)
# Após login, o utilizador submete o código TOTP para receber o token JWT
@auth_router.post("/verify-2fa")
def verify_2fa(data: TOTPVerifyRequest):
    user = get_user_by_email(data.email)
    if not user or not verify_totp_token(user.totp_secret, data.token):
        raise HTTPException(status_code=401, detail="Código TOTP inválido")
    
    # Geração do token JWT com email e role no payload
    jwt_token = create_jwt_token({"sub": user.email, "role": user.role})
    return {"access_token": jwt_token, "token_type": "bearer"}