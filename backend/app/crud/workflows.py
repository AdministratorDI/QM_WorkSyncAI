from sqlalchemy.orm import Session
from app.models.workflow import Workflow  # Modelo ORM para Workflow
from app.schemas import WorkflowCreate  # Schema de criação

# Criar um novo workflow
def create_workflow(db: Session, workflow_data: WorkflowCreate):
    db_workflow = Workflow(**workflow_data.dict())
    db.add(db_workflow)
    db.commit()
    db.refresh(db_workflow)
    return db_workflow

# Obter lista de workflows
def get_workflows(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Workflow).offset(skip).limit(limit).all()

# Obter workflow por ID
def get_workflow_by_id(db: Session, workflow_id: int):
    return db.query(Workflow).filter(Workflow.id == workflow_id).first()
