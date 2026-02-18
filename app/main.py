from fastapi import FastAPI
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate

app = FastAPI()

@app.get("/")
async def root():
    return  {"message": "API running"}
