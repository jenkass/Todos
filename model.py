from typing import List, Optional
from fastapi import Form

from pydantic import BaseModel


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

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


class TodoItems(BaseModel):
    todos: List[TodoItem]
