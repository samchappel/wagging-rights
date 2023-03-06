from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Float, DateTime, ForeignKey)

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owners'
    __table_args__ (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    address = Column(String())
    phone = Column(Integer())
    email = Column(String())

    pets = relationship('Pet', backref=backref('pet'))

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Address: {self.address}"

class Pets(Base):
    __tablename__ = 'pets'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    age = Column(Integer())
    breed = Column(String())
    temperament = Column(String())
    favorite_treats = Column(String())
    special_needs = Column(String())

    owner_id = Column(Integer(), ForeignKey(owners.id))

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Species: {self.species}, "\
            + f"Breed: {self.breed}, "\
            + f"Temperament: {self.temperament}"

class Provider(Base):
    __tablename__ = 'providers'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    hourly_rate = Column(Float())

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Hourly Rate: {self.hourly_rate}"

class Service(Base):
    __tablename__ = 'services'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    pet_id = Column(Integer(), ForeignKey('pets.id'))
    provider_id = Column(Integer(), ForeignKey('providers.id'))
    appointment = Column(String()) #make appointment for dog-walking, drop-ins, or house-sitting
    start_date = Column(DateTime())
    end_date = Column(DateTime())
    status = Column(String())
    fee = Column(Float())
    notes = Column(String())


