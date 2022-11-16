from fastapi import APIRouter, HTTPException, status, Body, Path
from typing import List

from models.events import Event

event_router = APIRouter(tags=["Event"])

events = []


@event_router.get("/", response_model=List[Event])
async def get_all_events():
    return events


@event_router.get("/{event_id}")
async def get_one_event(event_id: int = Path(...)):
    for event in events:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Event not found!")


@event_router.post("/new")
async def add_one_event(body: Event = Body(...)):
    events.append(body)
    return {"message": "Event created successfully!"}


@event_router.delete("/{event_id}")
async def delete_one_event(event_id: int = Path(...)):
    for event in events:
        if event.id == event_id:
            events.remove(event)
            return {"message": "Event successfully deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Event not found")


@event_router.delete("/")
async def delete_all_events():
    events.clear()
    return {"message": "All events successfully deleted"}