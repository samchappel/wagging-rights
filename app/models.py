from sqlalchemy import create_engine, func
from sqlalchemy import (PrimaryKeyConstraint, Table, Column, String, Integer, Float, DateTime, ForeignKey)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pet(Base):
    __tablename__ = 'pets'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    age = Column(Integer())
    breed = Column(String())
    temperament = Column(String())
    favorite_treats = Column(String())
    notes = Column(String())

    owner_id = Column(Integer(), ForeignKey('owners.id'))

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Species: {self.species}, "\
            + f"Breed: {self.breed}, "\
            + f"Temperament: {self.temperament}"\
            + f"Owner ID: {self.owner_id}"

class Owner(Base):
    __tablename__ = 'owners'
    __table_args__= (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    address = Column(String())
    phone = Column(Integer())
    email = Column(String())
    hourly_rate = Column(Float())

    pets = relationship('Pet', backref=backref('pet'))

    def __repr__(self):
        return f"Id: {self.id}, "\
            + f"Name:{self.name}, "\
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Address: {self.address}"\

class Provider(Base):
    __tablename__ = 'providers'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    availability = Column(DateTime()) #how can we show availability?
    email = Column(String())
    phone = Column(Integer())
    hourly_rate = Column(Float())

    def __repr__(self):
        return f"Id: {self.id}, "\
            + f"Name:{self.name}, "\
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Hourly Rate: {self.hourly_rate}" #ask Sam what she thinks on a practical standpoint

class Service(Base):
    __tablename__ = 'services'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    pet_id = Column(Integer(), ForeignKey('pets.id'))
    provider_id = Column(Integer(), ForeignKey('providers.id'))
    request = Column(String()) #make appointment for dog-walking, drop-ins, or house-sitting
    start_date = Column(DateTime())
    end_date = Column(DateTime())
    status = Column(String())
    fee = Column(Float()) #total cost
    notes = Column(String())

    pet = relationship('Pet', backref=backref('pets'))
    provider = relationship('Provider', backref=backref('providers'))

    def __repr__(self):
        return f"Id: {self.id}, "\
            +f"Request: {self.request}, "\
            +f"Start Date: {self.start_date}, "\
            +f"End Date: {self.end_date}, "\
            +f"Fee: {self.fee}, "\
            +f"Notes: {self.notes}, "\


