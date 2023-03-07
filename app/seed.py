from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Pet, Owner, Service, Provider

if __name__ == '__main__':
    engine = create_engine('sqlite:///wagging_rights.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Pet).delete()
    session.query(Owner).delete()

    fake = Faker()

    dog_breeds = ["Husky", "Beagle", "German Shepherd", "Bulldog", "Labrador Retriever", "Golden Retriever", "Malamute", "Poodle", "Chihuahua" ]

    favorite_treats = ["scooby-snack", "zesty-paws", "milk-bones", "little-bites", "Pup-peroni", "Snausages"]

    owners = []

    temperaments = ["Assertive or Aggressive", "Neutral", "Passive"]

    for _ in range(20):
        owner = Owner(
            name = f"{fake.first_name()} {fake.last_name()}",
            email = fake.email(),
            phone = random.randint(1000000000, 9999999999),
            address = fake.address()
        )

        session.add(owner)
        session.commit()

        owners.append(owner)

    pets = []

    for owner in owners:

        for _ in range (random.randint(1,3)):
            rand_species = random.choice(species)

            pet = Pet(
                name = fake.name(),
                age = fake.age(),
                breed = random.choice(dog_breeds),
                temperament = random.choice(temperaments),
                favorite_treat = random.choice(favorite_treats),
                special_needs = 
            )