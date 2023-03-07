from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from datetime import datetime, timedelta

from models import Pet, Owner, Provider, Service, Base
from faker import Faker

# from faker import Faker
# import random

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from models import (Pet, Owner, Service, Provider)


fake = Faker()
if __name__ == '__main__':
    engine = create_engine('sqlite:///wagging_rights.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    start_date = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None)
    print(f"Start date: {start_date.strftime('%B %d, %Y')}")

    end_date = start_date + timedelta(days=random.randint(1, 7))
    print(f"End date: {end_date.strftime('%B %d, %Y')}")
    # end_date = fake.date_time_between_dates(start_date=start_date, end_date=start_date+timedelta(days=random.randint(1, 7)))
    # print(f"End date: {end_date.strftime('%d-%m-%Y')}")

    # while end_date < start_date:
    #     end_date = start_date + timedelta(days=random.randint(1, 7))

    # service = Service(
    #     request = random.choice(requests),
    #     start_date = start_date,
    #     end_date = end_date,
    #     notes=fake.sentence(),
    #     fee = provider.hourly_rate,
    #     provider_id = provider.id,
    #     pet_id = random.choice(pets).id
    # )

# start_date = fake.date_time_between(start_date='now', end_date='+7d')
# end_date = fake.date_time_between_dates(start_date=start_date, end_date=start_date+timedelta(days=random.randint(1, 7)))

    # Getting an Owner's Pets

#     # Use session.query and .first() to grab the first Owner
#     first_owner = session.query(Owner).first()

#     # Use session.query and filter_by to get the Owner's pets from Pet
#     owners_pets = session.query(Pet).filter_by(id=first_owner.id)

#     # Print out the Owner's pets
#     # print([pet for pet in owners_pets])

#     # Getting a Pet's Owner

#     # Use session.query and .first() to grab the first pet
#     first_pet = session.query(Pet).first()

#     # Use session.query and .filter_by() to get the owner associated with this pet
#     pet_owner = session.query(Owner).filter_by(id=first_pet.owner_id)

#     # print([owner for owner in pet_owner])

#     # 4. ✅ Head back to models.py to build out a Many to Many association
# #--------------------------------------------

# # 6. ✅ Many to Many

#     # Use session.query and .first() to get the first handler
#     first_handler = session.query(Handler).first()

#     # Use session.query and .filter_by() to grab the handler_jobs
#     handler_jobs = session.query(Job).filter_by(handler_id=first_handler.id)

#     # Handler Associated with Job
#     print([job for job in handler_jobs])

#     # Use 'handler_jobs' to query pets for the associated pet to each job
#     handler_pets = [session.query(Pet).get(job.pet_id) for job in handler_jobs]

#     # Pet Associated with Job
#     print([pet for pet in handler_pets])

# # from db.models import GroceryItem, Store, ShoppingCart

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
