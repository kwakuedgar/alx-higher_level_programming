#!/usr/bin/python3

"""
Contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    The State class maps <state object> to the <states table>

    Args:
        __tablename__ (str): name of the mapping table
        id (int): the unique id
        name (str): the value, name of a state

    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
