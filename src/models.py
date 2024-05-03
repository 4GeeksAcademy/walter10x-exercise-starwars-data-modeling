import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    name = Column(String)
    favourite_planets = relationship("FavouritePlanet", back_populates="user")
    favourite_characters = relationship("FavouriteCharacter", back_populates="user")

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    characters = relationship("Character", back_populates="planet")

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship("Planet", back_populates="characters")
    ships = relationship("Ship", back_populates="character")

class Ship(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship("Character", back_populates="ships")

class FavouritePlanet(Base):
    __tablename__ = 'favourite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship("User", back_populates="favourite_planets")
    planet = relationship("Planet")

class FavouriteCharacter(Base):
    __tablename__ = 'favourite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    user = relationship("User", back_populates="favourite_characters")
    character = relationship("Character")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
