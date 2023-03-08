#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Owner, Pet, Provider, Service

from helpers import update_pet, print_pet, add_new_pet

engine = create_engine('sqlite:///wagging_rights.db')
session = sessionmaker(bind=engine)()

YES = ['y', 'ye', 'yes']
NO = ['n','no']
if __name__ == '__main__':
    #Intro: welcome to the CLI, pick a store
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
    print("Welcome To Wagging Rights CLI!")
    print('')

    # Ask user to input their ID number (corresponds with owner_id)
    owner_id = int(input("Please Enter Your Owner Id To Get Started: "))

    # Use owner_id to query Owners table and return owner name.
    owner_name = session.query(Owner.name).filter(Owner.id == owner_id).first()[0].split(" ")[0]

    # Print Welcome, {Name} and prompt them to input whether they would like to manage pets or appointments.
    print('')
    print('')
    print('-'*50)
    print(f"Welcome, {owner_name}! What Would You Like To Do Today?")
    print('')
    print(f'PLEASE ENTER:')
    task = input(f"""pets - To View Your Pet(s) Profile
appointment - To Book An Appointment

ENTER: """).lower()

    # If 'Pets' bring user to 'Main Menu' pets.
    if task == "pets":
        print('')
        print('')
        print("Your Pet(s) Profile:")
        print('')

    # Use owner_id to query Pets table and return all pets associated with that owner.
        pets = session.query(Pet).filter(Pet.owner_id == owner_id).all()
        for pet in pets:
            print(pet)
        # TODO - We will reformat this printout later.

    # Prompt user to select from options to Add Pet, Update Pet, Remove Pet
        option = input("""
PLEASE ENTER:
add - Add A Pet
update - Update A Pet
remove - Remove A Pet

ENTER: """).lower()

        if option == "add":
            add = True
            while add:
                print('')
                print("Please Provide Information About Your New Pet!")
                print('')
                name = input("Name: ")
                age = int(input("Age: "))
                breed = input("Breed: ")
                temperament = input("Temperament: ")
                treats = input("Favorite Treats: ")
                notes = input("Additional Notes/Special Needs: ")
                add_new_pet(session, name, age, breed, temperament, treats, notes, owner_id)
                another = input("""
Would you like to add another pet? Yes/No: """).lower()
                if another == "no":
                    print("Routing you back to the main menu...")
                    add = False

        elif option == "update":
            update = True
            while update: 
                pet_id = input("You've selected update! Enter the ID of the pet you want to update: ")
                pet = session.query(Pet).filter(Pet.id == pet_id, Pet.owner_id == owner_id).first()
                if not pet:
                    print("Invalid ID. Please enter a valid ID that belongs to your pet.")
                    continue
                for pet in pets:
                    field = input(f"What updates would you like to make for {pet.name}? Enter 'name', 'age', 'breed', 'temperament', 'treats', or 'notes' to make those changes to {pet.name}'s record: ").lower()
                    if field not in ['name', 'age', 'breed', 'temperament', 'treats', 'notes']:
                        print("Invalid field. Please enter a valid field.")
                        continue

                new_value = input(f"Enter the new value for {field}: ")
                update_pet(session, pet, field, new_value)
                print_pet(pet)

                another = input("Would you like to update another pet? Yes/No: ").lower()
                if another == "no":
                    print("Routing you back to the main menu...")
                    update = False

        elif option == "remove":
            remove = True
            while remove:
                print('')
                pet_idx = int(input("Please Provide The 'Pet ID' Of The Pet You Wish To Remove: "))
                pets = session.query(Pet).filter(Pet.id == pet_idx).first()

                print('')
                print(pets)

                yes_no = input("Do You Wish To Delete This Pet? (Y/n): \n")
                if yes_no.lower() in YES:
                    session.delete(pets)
                    session.commit()
                    print('Your Pet Has been Removed Successfully!')
                    rem_another = input('Would you like to remove another pet? (Y/n): \n')
                    if rem_another.lower() in YES:
                        continue
                    elif rem_another.lower() in NO:
                        print("Routing you back to main menu...")
                        remove = False
                    else:
                        print("Invalid input. Routing you back to main menu...")
                        remove = False

                else:
                    print('Pet has not been deleted.')

                    #NEED TO MAKE REMOVE OPTION SO THAT USERS CAN DELETE THEIR OWN PETS ONLY AND NOT OTHER USERS PETS.
                    #Run python seeds.py to restore table data

        else:
            print("Invalid input.")


    elif task == "appointment":
        print("Yay, you chose 'appointments'! This feature is coming soon.")
    else:

        print("Invalid input.")

    # print('Thank you for using the Wagging Rights CLI!\n ')

