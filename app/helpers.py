from models import Pet, Service 



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




# def remove_pet(session, idx):


                # session.show(pet)
                # print('Do You Still Wish To Remove?')
                # new_db_pet = session.query(Pet).filter(Pet.id == id).first()
                # print('')
                # print('')
                # print('Thank You For Your Submission!')
                # print('')
                # print(new_db_pet)
                # print('Your Pet Has Been Removed Successfully!')



# from models import Service

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

def create_new_dropwalk(session, pet_id, request, start_date, fee):
    new_appt = Service(pet_id=pet_id, request=request, 
                    start_date=start_date, fee=fee)
    session.add(new_appt)
    session.commit()
    new_db_appt = session.query(Service).filter(Service.id == new_appt.id).first()
    print(new_db_appt)