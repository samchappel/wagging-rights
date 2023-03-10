from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import (Pet, Owner, Service, Provider)
from faker import Faker
from datetime import timedelta
import random


if __name__ == '__main__':
    engine = create_engine('sqlite:///wagging_rights.db')
    fake = Faker()
    Session = sessionmaker(bind=engine)
    session = Session()


#DELETE PET,OWNER,PROVIDER,SERVICE; CLEAR DATA ON INITIATION
    session.query(Pet).delete()
    session.query(Owner).delete()
    session.query(Provider).delete()
    session.query(Service).delete()

    dog_breeds = ["Husky", "Beagle", "German Shepherd", "Bulldog", "Labrador Retriever", "Golden Retriever", "Malamute", "Poodle", "Chihuahua" ]
    favorite_treats = ["scooby-snack", "zesty-paws", "milk-bones", "little-bites", "Pup-peroni", "Snausages"]
    temperaments = ["Assertive or Aggressive", "Neutral", "Passive"]


    owners = []
    for _ in range(30):
        owner = Owner(
            name = f"{fake.first_name()} {fake.last_name()}",
            email = fake.email(),
            phone = random.randint(1000000000, 9999999999),
            address = fake.address()
        )
        session.add(owner) #adds owner to session
        session.commit() #sets change to session
        owners.append(owner) #add owner to list of "owners"


    pets = []
    for owner in owners:
        for _ in range (random.randint(1,3)):
            pet = Pet(
                name = fake.first_name(),
                age = random.randint(1,10),
                breed = random.choice(dog_breeds),
                temperament = random.choice(temperaments),
                favorite_treats = random.choice(favorite_treats),
                notes = fake.sentence(),
                owner_id = owner.id,
            )
            session.add(pet)
            session.commit()
            pets.append(pet)

        session.query(Provider).delete()
        session.query(Service).delete()
        providers = []
        for _ in range(10):
            date = fake.date_time_between(start_date="now", end_date="+3d", tzinfo=None)
            end_date = timedelta(days=random.randint(1, 1))
            provider = Provider(
                name = f"{fake.first_name()} {fake.last_name()}",
                email = fake.email(),
                phone = random.randint(1000000000, 9999999999),
                availability = f"""
{fake.day_of_week()} \n
{fake.day_of_week()} \n
{fake.day_of_week()} \n
""")
            session.add(provider)
            session.commit()
            providers.append(provider)


        requests = ['Walk', 'Drop-in', 'House-Sit']
        services = []
        for provider in providers:
            for _ in range(random.randint(1,10)):
                date = fake.date_time_between(start_date="now", end_date="+1y", tzinfo=None)
                service = Service(
                    request = random.choice(requests),
                    start_date = date,
                    end_date = date + timedelta(days=random.randint(1, 3)),
                    notes=fake.sentence(),
                    fee = f'$' + f'%.2f' % random.uniform(20,40),
                    provider_id = provider.id,
                    pet_id = random.choice(pets).id,
                )
                services.append(service)
    session.bulk_save_objects(services)
    session.commit()
    session.close()