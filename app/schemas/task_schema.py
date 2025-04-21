from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: bool

class TaskOut(TaskBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime  # ✅ Add this

    class Config:
        orm_mode = True
