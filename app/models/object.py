from pydantic import BaseModel

class ObjectModel(BaseModel):
    id: str
    full_name: str
    email: str
    mobile_number: str

    class Config:
        extra = 'forbid'