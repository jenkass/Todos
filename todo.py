from fastapi import APIRouter, Path
from model import Todo, TodoItem

todo_router = APIRouter()
todo_list = []


@todo_router.get("/todo")
async def get_todo():
    return {"todos": todo_list}


@todo_router.post("/todo")
async def add_todo(todo: Todo):
    todo_list.append(todo)
    return {"message": "Todo successfully added"}


@todo_router.get("/todo/{todo_id}")
async def get_one_todo(todo_id: int = Path(..., title="the id of the todo to retrieve")):
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": f"not found Todo with this id {todo_id}"}


@todo_router.put("/todo/{todo_id}")
async def update_one_todo(todo_data: TodoItem, todo_id: int = Path(...)):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated"}

    return {"message": "Todo wasn't update"}


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
    return {"message": "Not found for delete"}
