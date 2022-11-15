from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []
templates = Jinja2Templates(directory="templates/")


@todo_router.get("/todo", response_model=TodoItems)
async def get_todo(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "todos": todo_list})


@todo_router.post("/todo", status_code=201)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html", {"requset": request, "todos": todo_list})


@todo_router.get("/todo/{todo_id}")
async def get_one_todo(request: Request, todo_id: int = Path(..., title="the id of the todo to retrieve")):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html", {"request": request, "todo": todo})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@todo_router.put("/todo/{todo_id}")
async def update_one_todo(todo_data: TodoItem, todo_id: int = Path(...)):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@todo_router.delete("/todo")
async def delete_todos():
    todo_list.clear()
    return {"message": "Delete todos"}


@todo_router.delete("/todo/{todo_id}")
async def delete_one_todo(todo_id: int = Path(...)):
    i = 0
    for todo in todo_list:
        if todo.id == todo_id:
            todo_list.pop(i)
            return {"message": "Todo successfully deleted"}
        i += 1
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
