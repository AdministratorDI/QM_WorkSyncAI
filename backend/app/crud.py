
from sqlalchemy.orm import Session
from app.models.models import User, Workflow, ExecutionLog, Suggestion
from app.schemas import user as user_schema, workflow as workflow_schema, log as log_schema, suggestion as suggestion_schema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ==============================
# User CRUD
# ==============================

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, totp_secret=user.totp_secret, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ==============================
# Workflow CRUD
# ==============================

def get_workflows(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Workflow).offset(skip).limit(limit).all()

def create_workflow(db: Session, workflow: workflow_schema.WorkflowCreate):
    db_workflow = Workflow(**workflow.dict())
    db.add(db_workflow)
    db.commit()
    db.refresh(db_workflow)
    return db_workflow


# ==============================
# Execution Log CRUD
# ==============================

def get_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ExecutionLog).offset(skip).limit(limit).all()

def create_log(db: Session, log: log_schema.ExecutionLogCreate):
    db_log = ExecutionLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


# ==============================
# Suggestion CRUD
# ==============================

def get_suggestions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Suggestion).offset(skip).limit(limit).all()

def create_suggestion(db: Session, suggestion: suggestion_schema.SuggestionCreate):
    db_suggestion = Suggestion(**suggestion.dict())
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion
