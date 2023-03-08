#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///wagging_rights.db')
session = sessionmaker(bind=engine)()

from models import Owner, Pet, Provider, Service


if __name__ == '__main__':
    print('''
__          __     _____  _____ _____ _   _  _____   _____  _____ _____ _    _ _______ _____ _
\ \        / /\   / ____|/ ____|_   _| \ | |/ ____| |  __ \|_   _/ ____| |  | |__   __/ ____| |
 \ \  /\  / /  \ | |  __| |  __  | | |  \| | |  __  | |__) | | || |  __| |__| |  | | | (___ | |
  \ \/  \/ / /\ \| | |_ | | |_ | | | | . ` | | |_ | |  _  /  | || | |_ |  __  |  | |  \___ \| |
   \  /\  / ____ \ |__| | |__| |_| |_| |\  | |__| | | | \ \ _| || |__| | |  | |  | |  ____) |_|
    \/  \/_/    \_\_____|\_____|_____|_| \_|\_____| |_|  \_\_____\_____|_|  |_|  |_| |_____/(_)

                                        |\_/|
                                        | @ @   Woof!
                                        |   <>              _
                                        |  _/\------____ ((| |))
                                        |               `--' |
                                    ____|_       ___|   |___.'
                                    /_/_____/____/_______|

    ''')
    
    print("Welcome to the Wagging Rights CLI!")

    # Ask user to input their ID number (corresponds with owner_id)
    owner_id = int(input("Please enter your owner id: "))

    # Use owner_id to query Owners table and return owner name.
    owner_name = session.query(Owner.name).filter(Owner.id == owner_id).first()[0].split(" ")[0]

    # Print Welcome, {Name} and prompt them to input whether they would like to manage pets or appointments.
    print(f"Welcome, {owner_name}! What would you like to do?")
    task = input("What would you like to do? Enter 'pets' to manage pets or 'appointments' to manage appointments: ").lower()

    # If 'Pets' bring user to 'Main Menu' pets.
    if task == "pets":
        print("Here are your pets:")

    # Use owner_id to query Pets table and return all pets associated with that owner.
        pets = session.query(Pet).filter(Pet.owner_id == owner_id).all()
        for pet in pets:
            print(pet)
        # TODO - We will reformat this printout later.

    # Prompt user to select from options to Add Pet, Update Pet, Remove Pet
        option = input("What would you like to do? Enter 'add' to add a pet, 'update' to update a pet, 'remove' to remove a pet: ").lower()

        if option == "add":
            # BIANCA - Write your code here! :-)
            print("You're adding a pet!")
            
        elif option == "update":
            pet_id = input("You've selected update! Enter the ID of the pet you want to update: ")
            pet = session.query(Pet).filter(Pet.id == Pet.id)
            for pet in pets:
                update = input(f"What updates would you like to make for {pet.name}? Enter 'name', 'age', 'breed', 'temperament', 'treats', or 'notes' to make those changes for {pet.name}: ").lower()
                if update == "name":
                    new_name = input("Enter a new name: ")
                    pet.name = new_name
                    print(f"{pet.name}'s name has been updated.")
                elif update == "age":
                    new_age = input("Enter a new age: ")
                    pet.age = int(new_age)
                    print(f"{pet.name}'s age has been updated to {pet.age}.")
                elif update == "breed":
                    new_breed = input("Enter a new breed: ")
                    pet.breed = new_breed
                    print(f"{pet.name}'s breed has been updated to {pet.breed}.")
                elif update == "temperament":
                    new_temperament = input("Enter a new temperament: ")
                    pet.temperament = new_temperament
                    print(f"{pet.name}'s temperament has been updated to {pet.temperament}.")
                elif update == "treats":
                    new_treats = input("Enter new favorite treat: ")
                    pet.treats = new_treats
                    print(f"{pet.name}'s favorite treat have been updated to {pet.treat}.")
                elif update == "notes":
                    new_notes = input("Enter new note: ")
                    pet.notes = new_notes
                    print(f"{pet.name}'s notes have been updated to '{pet.notes}'.")
                else:
                    print("Invalid choice. Please enter a field to update from the list above.")

        elif option == "remove":
            # TERRENCE - Write your code here! :-)
            print("You're removing a pet!")
        else:
            print("Invalid input.")


    elif task == "appointments":
        print("Yay, you chose 'appointments'! This feature is coming soon.")
    else:
        print("Invalid input.")

    

    



    

    

