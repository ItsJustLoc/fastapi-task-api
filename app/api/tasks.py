from fastapi import APIRouter, Depends

from app.api.deps import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskRead

router = APIRouter()

@router.post("/tasks", response_model=TaskRead, status_code=201)
async def newTask(task_in: TaskCreate, db = Depends(get_db)):
    new_task = Task(title=task_in.title, completed= task_in.completed)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
