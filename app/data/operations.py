import json
from typing import List, Optional
from app.models.object import ObjectModel

# Global data list (in-memory)
data: List[ObjectModel] = []

def load_objects_from_json(file_path: str) -> None:
    """Loads objects from the JSON file into the global data list."""
    global data  # Modify the global data variable
    try:
        with open(file_path, "r") as f:
            data = [ObjectModel(**item) for item in json.load(f)]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

def add_object(new_object: ObjectModel) -> None:
    # Check if an object with the same id already exists
    for obj in data:
        if obj.id == new_object.id:
            return None
            
    # Add the new object to the global data list
    data.append(new_object)
    return new_object

def delete_object(object_id: str) -> Optional[ObjectModel]:
    # Delete an object by ID from the global data list
    # Returns the deleted object if found, otherwise None

    global data
    for obj in data:
        if obj.id == object_id:
            data.remove(obj)
            return obj
    # print(f"Object with id {object_id} not found.")
    return None


load_objects_from_json("objects.json")