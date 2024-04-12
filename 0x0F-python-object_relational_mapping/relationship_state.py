#!/usr/bin/python3
"""Defines the State model for a MySQL database, including a relationship with
the City model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        id (int): The state's ID (primary key).
        name (str): The state's name (not nullable, max 128 chars).
        cities (relationship): The state's related cities (one-to-many).
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
