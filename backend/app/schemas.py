from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# Schemas para Workflow
class WorkflowBase(BaseModel):
    name: str
    description: Optional[str] = None
    trigger: str
    action: str
    condition: Optional[str] = None
    is_active: Optional[bool] = True


class WorkflowCreate(WorkflowBase):
    pass


class WorkflowUpdate(WorkflowBase):
    pass


class WorkflowResponse(WorkflowBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Schemas para ExecutionLog
class ExecutionLogBase(BaseModel):
    workflow_id: int
    result: str
    suggestion: Optional[str] = None


class ExecutionLogCreate(ExecutionLogBase):
    pass


class ExecutionLogResponse(ExecutionLogBase):
    id: int
    executed_at: datetime

    class Config:
        orm_mode = True


# Schemas com relações
class WorkflowWithLogs(WorkflowResponse):
    logs: List[ExecutionLogResponse] = []


# Schemas para autenticação e utilizador
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    role: Optional[str] = "user"


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class UserCreate(RegisterRequest, UserBase):
    pass


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    user_id: Optional[int] = None


class TOTPVerify(BaseModel):
    user_id: int
    totp_code: str
