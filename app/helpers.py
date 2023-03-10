from models import Pet, Service
from datetime import datetime, time

def add_new_pet(session, name, age, breed, temperament, treats, notes, owner_id):
    new_pet = Pet(name=name, age=age, breed=breed, temperament=temperament,
                favorite_treats=treats, notes=notes, owner_id=owner_id)
    session.add(new_pet)
    session.commit()
    new_db_pet = session.query(Pet).filter(Pet.id == new_pet.id).first()
    print('')
    print('')
    print("Thank you for your submission! Your pet has been added successfully. \nHere is the information we received:")
    print('')
    print(new_db_pet)

def update_pet(session, pet, field, new_value):
    if field == "name":
        pet.name = new_value
    elif field == "age":
        pet.age = int(new_value)
    elif field == "breed":
        pet.breed = new_value
    elif field == "temperament":
        pet.temperament = new_value
    elif field == "treats":
        pet.favorite_treats = new_value
    elif field == "notes":
        pet.notes = new_value
    else:
        print("Invalid field. Please enter a valid field.")
        return
    session.commit()
    print(f"{pet.name}'s {field} has been updated to {new_value}.")


def print_pet(pet):
    print(f"ID: {pet.id}")
    print(f"Name: {pet.name}")
    print(f"Age: {pet.age}")
    print(f"Breed: {pet.breed}")
    print(f"Temperament: {pet.temperament}")
    print(f"Treats: {pet.favorite_treats}")
    print(f"Notes: {pet.notes}")

def query_pets(session, owner_id):
    pets = session.query(Pet).filter(Pet.owner_id == owner_id).all()
    for pet in pets:
                print(pet)

def create_new_dropwalk(session, pet_id, request, start_date, fee, notes):
    new_appt = Service(pet_id=pet_id, request=request, 
                    start_date=start_date, fee=fee, notes=notes)
    session.add(new_appt)
    session.commit()
    new_db_appt = session.query(Service).filter(Service.id == new_appt.id).first()
    print(f"""Thank you! Here is the appointment information we received: 
{new_db_appt}""")
    print("Your appointment is pending until reviewed by a provider.")

def book_house_sitting(session, pet_id, start_date, end_date, notes):
    start_datetime = datetime.combine(start_date, time.min)
    end_datetime = datetime.combine(end_date, time.min)
    
    days_of_service = (end_date - start_date).days
    fee = days_of_service * 70

    print(f"pet_id: {pet_id}")
    print(f"start_date: {start_datetime}")
    print(f"end_date: {end_datetime}")
    print(f"notes: {notes}")
    print(f"request: House-Sit")
    print(f"fee: ${fee}.00")
    
    service = Service(pet_id=pet_id, start_date=start_datetime, end_date=end_datetime, notes=notes, request="House-Sit", fee=f"${fee:.2f}")
    try:
        # add the new service object to the session and commit the changes
        session.add(service)
        session.commit()
        # print the details of the newly added service object
        print(f"""Thank you! Here is the appointment information we received: 
{service}""")
        print("Your appointment is pending until reviewed by a provider.")

    except Exception as e:
        # print any errors that occur during the commit process
        print(f"Error adding service to database: {e}")
        session.rollback()

# NEW - Bianca - ID error handling helper function.
def check_id(session, Table, integer):
     db_ids = session.query(Table.id).all()
     all_ids = [id[0] for id in db_ids]
     return integer in all_ids
# END - Bianca - Owner_ID error handling helper function.
