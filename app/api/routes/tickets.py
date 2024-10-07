from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import app.db_models.crud as crud
from app.api_models.tickets import TicketCreate, TicketResponse, TicketListResponse
from app.db_models.base import Ticket
from app.api.dependencies.sqldb import get_db

router = APIRouter()

@router.post("/", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = crud.create_ticket(db, ticket.title, ticket.description, ticket.project_id, ticket.status, ticket.priority)
    return db_ticket

@router.get("/", response_model=TicketListResponse)
def read_tickets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tickets = crud.get_tickets(db, skip, limit)
    return TicketListResponse(tickets=[TicketResponse.from_orm(ticket) for ticket in tickets])

@router.get("/{ticket_id}", response_model=TicketResponse)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db, ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.put("/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db, ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return crud.update_ticket(db, ticket_id, ticket.title, ticket.description, ticket.project_id, ticket.status, ticket.priority)

@router.delete("/{ticket_id}", response_model=TicketResponse)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db, ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {'message': f'Ticket with id {ticket_id} deleted'}