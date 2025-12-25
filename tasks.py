from fastapi import APIRouter, Depends, HTTPException
from app.schemas.task import TaskCreate, Task
from typing import List

router = APIRouter()

tasks_db = []

@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    task_id = len(tasks_db) + 1
    task_data = task.dict()
    task_data.update({"id": task_id})
    tasks_db.append(task_data)
    return task_data

@router.get("/", response_model=List[Task])
def get_tasks():
    return tasks_db
