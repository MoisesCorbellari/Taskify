from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    title: str
    description: str
    created: date
    completed: bool


class TaskRequest(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    description: Optional[str] = Field(None, max_length=255) # noqa
    completed: bool = Field(default=False)
