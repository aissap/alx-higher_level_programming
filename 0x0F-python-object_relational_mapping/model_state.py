#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mydata = MetaData()
Base = declarative_base()

class State(Base):
    """
    State class that represents the states table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

