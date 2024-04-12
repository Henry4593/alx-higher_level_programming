#!/usr/bin/python3
"""Defines the City model for a MySQL database."""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (int): The city's ID (primary key).
        name (str): The city's name (not nullable, max 128 chars).
        state_id (int): The city's state ID (foreign key to states.id).
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
