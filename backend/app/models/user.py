from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

# Criação da base declarativa para os modelos ORM
Base = declarative_base()

class User(Base):
    __tablename__ = "users"  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)  # ID único do utilizador (chave primária)
    email = Column(String, unique=True, index=True, nullable=False)  # Email do utilizador, deve ser único
    hashed_password = Column(String, nullable=False)  # Palavra-passe já encriptada com hash
    totp_secret = Column(String, nullable=False)  # Segredo TOTP para 2FA (autenticação de dois fatores)
    role = Column(String, default="user")  # Papel do utilizador na plataforma (ex: user, admin)
    is_active = Column(Boolean, default=True)  # Estado de atividade do utilizador (ativo/inativo)