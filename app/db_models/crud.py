from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db_models.base import Project, Ticket

def create_project(db: Session, name: str, description: str) -> Project:
    try:
        project = Project(name=name, description=description)
        db.add(project)
        db.commit()
        db.refresh(project)
        return project
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_project(db: Session, project_id: int) -> Project:
    try:
        return db.query(Project).filter(Project.id == project_id).first()
    except SQLAlchemyError as e:
        raise e

def update_project(db: Session, project_id: int, name: str, description: str) -> Project:
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        if project:
            project.name = name
            project.description = description
            db.commit()
            db.refresh(project)
        return project
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def delete_project(db: Session, project_id: int):
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        if project:
            db.delete(project)
            db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    

def create_ticket(db: Session, title: str, description: str, project_id: int, status: str, priority: str) -> Ticket:
    try:
        ticket = Ticket(title=title, description=description, project_id=project_id, status=status, priority=priority)
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
def get_tickets(db: Session, skip: int = 0, limit: int = 10) -> List[Ticket]:
    try:
        return db.query(Ticket).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        raise e


def get_ticket(db: Session, ticket_id: int) -> Ticket:
    try:
        return db.query(Ticket).filter(Ticket.id == ticket_id).first()
    except SQLAlchemyError as e:
        raise e
    
def update_ticket(db: Session, ticket_id: int, title: str, description: str, project_id: int, status: str, priority: str) -> Ticket:
    try:
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if ticket:
            ticket.title = title
            ticket.description = description
            ticket.status = status
            ticket.priority = priority
            db.commit()
            db.refresh(ticket)
        return ticket
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
def delete_ticket(db: Session, ticket_id: int):
    try:
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if ticket:
            db.delete(ticket)
            db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e
