

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ⚠️ Substituir pela tua URI de ligação
DATABASE_URL = "postgresql://admin:admin123@localhost:5432/worksync_ai_db"

# Criar o engine
engine = create_engine(DATABASE_URL)

# Criar uma sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos SQLAlchemy
Base = declarative_base()