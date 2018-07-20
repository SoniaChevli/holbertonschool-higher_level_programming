#!/usr/bin/python3
'''
class definition of City
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State



class City(Base):
    ''' city class '''
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False,
    )
