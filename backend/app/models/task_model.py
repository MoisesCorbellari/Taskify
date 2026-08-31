from datetime import date

from shared.database import Base
from sqlalchemy import Boolean, Column, Date, Integer, String, Text


class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        Integer, 
        primary_key=True, 
        autoincrement=True)
    
    title = Column(
        String(255), 
        nullable=False)
    
    description = Column(
        Text, 
        nullable=True)
    
    created = Column(
        Date, 
        nullable=False, 
        default=date.today)
    
    completed = Column(
        Boolean, 
        nullable=False, 
        default=False)

    