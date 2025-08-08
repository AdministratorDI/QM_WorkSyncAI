


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from backend.database.database import SessionLocal
from backend.database.models.workflow import Workflow, Step
from backend.database.schemas.workflow import WorkflowCreate, WorkflowRead
import uuid
from datetime import datetime

router = APIRouter(
    prefix="/workflows",
    tags=["workflows"]
)

# Dependência para obter sessão da base de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=WorkflowRead)
def create_workflow(workflow: WorkflowCreate, db: Session = Depends(get_db), lang: str = "pt"):
    new_workflow = Workflow(
        id=uuid.uuid4(),
        name=workflow.name,
        description=workflow.description,
        status=workflow.status,
        created_at=datetime.utcnow()
    )
    db.add(new_workflow)
    db.flush()  # para obter o ID do workflow antes de adicionar os steps

    for step in workflow.steps:
        db_step = Step(
            id=uuid.uuid4(),
            name=step.name,
            step_order=step.step_order,
            type=step.type,
            config=step.config,
            workflow_id=new_workflow.id,
            created_at=datetime.utcnow()
        )
        db.add(db_step)

    db.commit()
    db.refresh(new_workflow)
    return new_workflow


@router.get("/", response_model=List[WorkflowRead])
def list_workflows(db: Session = Depends(get_db)):
    return db.query(Workflow).all()


@router.get("/{workflow_id}", response_model=WorkflowRead)
def get_workflow(workflow_id: UUID, db: Session = Depends(get_db), lang: str = "pt"):
    workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
    if not workflow:
        detail = "Workflow não encontrado." if lang == "pt" else "Workflow not found."
        raise HTTPException(status_code=404, detail=detail)
    return workflow