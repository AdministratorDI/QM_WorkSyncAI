from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models
from app.routers import workflows, logs, suggestions
from app.routes import notification
from app.routes import auth

# Inicialização da aplicação
app = FastAPI(
    title="WorkSync AI API",
    description="API para gestão de workflows automatizados com IA.",
    version="1.0.0",
    docs_url="/docs"
)

# Configuração do CORS
origins = [
    "http://localhost:3000",
    "https://www.worksyncai.dibrand.pt",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criação das tabelas (apenas para ambiente de desenvolvimento)
# Em produção, recomenda-se o uso de migrações com Alembic
Base.metadata.create_all(bind=engine)

# Inclusão de routers
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(workflows.router, prefix="/workflows", tags=["Workflows"])
app.include_router(logs.router, prefix="/logs", tags=["Logs de Execução"])
app.include_router(suggestions.router, prefix="/suggestions", tags=["Sugestões"])
app.include_router(notification.router, prefix="/notifications", tags=["Notificações"])

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "WorkSync AI API - Online"}
