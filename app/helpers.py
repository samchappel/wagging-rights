from models import Pet 

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