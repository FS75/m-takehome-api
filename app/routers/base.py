from typing import List
from fastapi import APIRouter, HTTPException
from app.models.object import ObjectModel
from app.data.operations import data, add_object, delete_object

router = APIRouter()

@router.get("/{object_id}", response_model=ObjectModel)
def get_object(object_id: str):
    """Retrieve an object by ID from the in-memory data list."""
    for obj in data:
        if obj.id == object_id:
            return obj
    raise HTTPException(status_code=404, detail=f"Object with id {object_id} not found")

@router.get("/", response_model=List[ObjectModel])
def get_all_objects():
    """Retrieve all objects from the in-memory data list."""
    if data:
        return data

    raise HTTPException(status_code=404, detail="No objects found")

@router.post("/", status_code=200)
def create_object(new_object: ObjectModel):
    """Add a new object to the in-memory data list."""
    add_object(new_object)
    return {"message": "Object added", "object": new_object}

@router.delete("/{object_id}", status_code=200)
def remove_object(object_id: str):
    """Delete an object by ID from the in-memory data list."""
    deleted_obj = delete_object(object_id)
    if not deleted_obj:
        raise HTTPException(status_code=404, detail="Object not found")
    return {"message": f"Object with ID {object_id} deleted", "object": deleted_obj}