from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TicketCreate(BaseModel):
    title: str
    description: Optional[str] = None
    project_id: int # is project_id needed?
    status: str
    priority: str

    class Config:
        from_attributes = True

class TicketResponse(TicketCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TicketListResponse(BaseModel):
    tickets: List[TicketResponse]

    class Config:
        from_attributes = True