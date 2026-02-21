from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

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

@router.get("/tasks", response_model=list[TaskRead])
async def getAllTasks(db = Depends(get_db)):
    tasks = db.scalars(select(Task).order_by(Task.id.desc())).all()
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskRead)
async def getTask(task_id: int, db = Depends(get_db)):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
