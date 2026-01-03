from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas

router = APIRouter()

fake_tasks = []

@router.post("/")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    fake_tasks.append(task)
    return {"message": "Task created", "task": task}

