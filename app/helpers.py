from models import Pet

def add_new_pet(session, name, age, breed, temperament, treats, notes, owner_id):
    new_pet = Pet(name=name, age=age, breed=breed, temperament=temperament, 
                favorite_treats=treats, notes=notes, owner_id=owner_id)
    session.add(new_pet)
    session.commit()
    new_db_pet = session.query(Pet).filter(Pet.id == new_pet.id).first()
    print("Thank you for your submission. Here is the information we received:")
    print(new_db_pet)
