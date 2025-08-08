

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.auth import create_access_token
import sqlite3
from passlib.hash import bcrypt

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

def get_user_by_email(email: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, password FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "email": row[1], "hashed_password": row[2]}
    return None

@router.post("/login")
def login(data: LoginRequest):
    user = get_user_by_email(data.email)
    if not user or not bcrypt.verify(data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": user["email"]})
    return {"token": token}

# --- Novos endpoints ---
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Request
import os

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class RegisterRequest(BaseModel):
    email: str
    password: str

def create_user(email: str, password: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, bcrypt.hash(password)))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email já registado.")
    finally:
        conn.close()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest):
    create_user(data.email, data.password)
    return {"message": "Utilizador criado com sucesso."}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return {"email": email}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

@router.get("/me")
def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

@router.post("/logout")
def logout(request: Request):
    # Logout simbólico. O frontend deve apagar o token manualmente.
    return {"message": "Sessão terminada. Por favor apague o token localmente."}