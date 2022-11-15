from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

app.include_router(todo_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


