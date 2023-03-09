from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from datetime import datetime, timedelta

from models import Pet, Owner, Provider, Service, Base
from faker import Faker


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


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
