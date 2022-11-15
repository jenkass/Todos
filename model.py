from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        Schema_extra = {
            "Example": {
                "id": 1,
                "item": {
                    "item": "Example schema!"
                }
            }
        }


class TodoItem(BaseModel):
    item: str