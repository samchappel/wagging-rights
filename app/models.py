from sqlalchemy import create_engine
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, DateTime, ForeignKey)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///wagging_rights.db', echo=True)

Base = declarative_base()

#PET, OWNER, PROVIDER, SERVICE CLASSES
class Pet(Base):
    __tablename__ = 'pets'
    __table_args__ = (PrimaryKeyConstraint('id'),)
    __mapper_args__ = {'confirm_deleted_rows': False}

    id = Column(Integer())
    name = Column(String())
    age = Column(Integer())
    breed = Column(String())
    temperament = Column(String())
    favorite_treats = Column(String())
    notes = Column(String())
    owner_id = Column(Integer(), ForeignKey('owners.id'))

    def __repr__(self):
        line = '-'*50
        return f"Pet ID: {self.id}, \n" \
            + f"Name: {self.name}, \n" \
            + f"Age: {self.age}, \n" \
            + f"Breed: {self.breed}, \n" \
            + f"Temperament: {self.temperament}, \n" \
            + f"Treats: {self.favorite_treats}, \n" \
            + f"Notes: {self.notes}, \n" \
            + f"Owner ID: {self.owner_id} \n" \
            + f"\n" \
            + f"{line}" \
            + f"\n" \

class Owner(Base):
    __tablename__ = 'owners'
    __table_args__= (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    address = Column(String())
    phone = Column(Integer())
    email = Column(String())

    pets = relationship('Pet', backref=backref('pet'))

    def __repr__(self):
        return f"Owner ID: {self.id}, "\
            + f"Name:{self.name}, "\
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Address: {self.address}"\

class Provider(Base):
    __tablename__ = 'providers'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    availability = Column(String())
    email = Column(String())
    phone = Column(Integer())
    # hourly_rate = Column(String())

    def __repr__(self):
        return f"Provider ID: {self.id}, "\
            + f"Name:{self.name}, "\
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Availability: {self.availability}"\
            # + f"Hourly Rate: {self.hourly_rate}"\

class Service(Base):
    __tablename__ = 'services'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    pet_id = Column(Integer(), ForeignKey('pets.id'))
    provider_id = Column(Integer(), ForeignKey('providers.id'))
    request = Column(String()) #make appointment for dog-walking, drop-ins, or house-sitting
    start_date = Column(DateTime())
    end_date = Column(DateTime())
    fee = Column(String()) #total cost
    notes = Column(String())

    pet = relationship('Pet', backref=backref('pets'))
    provider = relationship('Provider', backref=backref('providers'))

    def __repr__(self):
        return f"Service ID: {self.id}, \n"\
            +f"Pet ID: {self.pet_id}, \n"\
            +f"Provider ID: {self.provider_id}, \n"\
            +f"Request: {self.request}, \n"\
            +f"Start Date: {self.start_date}, \n"\
            +f"End Date: {self.end_date}, \n"\
            +f"Fee: {self.fee}, \n"\
            +f"Notes: {self.notes} \n"\


