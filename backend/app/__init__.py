# Inicialização do pacote app

from fastapi import FastAPI
from app.routes import auth, workflows, logs, suggestions
from app.database import engine, Base

# Criar as tabelas na base de dados se ainda não existirem
Base.metadata.create_all(bind=engine)

# Instância principal da aplicação FastAPI
app = FastAPI(
    title="WorkSync AI",
    description="API para gestão de workflows com suporte a IA e autenticação segura",
    version="1.0.0"
)

# Inclusão das rotas
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(workflows.router, prefix="/workflows", tags=["Workflows"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])
app.include_router(suggestions.router, prefix="/suggestions", tags=["Sugestões"])
