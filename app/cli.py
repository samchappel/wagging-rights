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
            add = True
            while add:
                print("Please provide some information about your new pet.")
                name = input("Name: ")
                age = int(input("Age: "))
                breed = input("Breed: ")
                temperament = input("Temperament: ")
                treats = input("Favorite Treats: ")
                notes = input("Additional Notes/Special Needs: ")
                new_pet = Pet(name=name, age=age, breed=breed, 
                              temperament=temperament, favorite_treats=treats, notes=notes, owner_id=owner_id)
                session.add(new_pet)
                session.commit()
                new_db_pet = session.query(Pet).filter(Pet.id == new_pet.id).first()
                print("Thank you for your submission. Here is the information we received:")
                print(new_db_pet)
                another = input("Would you like to add another pet? Yes/No: ").lower()
                if another == "no":
                    print("Routing you back to the main menu...")
                    add = False
        
        elif option == "update":
            # SAM - Write your code here! :-)
            print("You're updating a pet!")

        elif option == "remove":
            # TERRENCE - Write your code here! :-)
            print("You're removing a pet!")
        else:
            print("Invalid input.")


    elif task == "appointments":
        print("Yay, you chose 'appointments'! This feature is coming soon.")
    else:
        print("Invalid input.")

    

    



    

    

