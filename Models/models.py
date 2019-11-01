from flask import Flask 
from SQLAlchemy import Column 
from SQLAlchemy import Integer 
from SQLAlchemy import Stirng

from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


DB_URI = 'sqlite///./main.db'

Base = declarative_base()

class Note(Base):
    __tablename__ = 'Notes'
    
    id = Column(Integer, primary_key = True)
    title = Column(String(200))
    description = Column(String(200))
    create_at = Column(String(50))
    create_by = Column(String(50))
    priority = Column(Integer)
 
 
 
    if __name_ == __main__:
        
        from SQLAlchemy import create_engine 
        
        engine = create_engine(DB_URI)
        Base.metada.drop_all(engine)
        Base.metada.create_all(engine)
        
        

