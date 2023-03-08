#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Owner, Pet, Provider, Service
from helpers import add_new_pet
# from helpers import (create_store_table, create_wagging_rights_item_table, fill_cart, show_cart, remove_from_cart, collect_payment)
import click

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
    print('')
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
            # BIANCA - Write your code here! :-)
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
                # new_pet = Pet(name=name, age=age, breed=breed,
                #               temperament=temperament, favorite_treats=treats, notes=notes, owner_id=owner_id)
                # session.add(new_pet)
                # session.commit()
                # new_db_pet = session.query(Pet).filter(Pet.id == new_pet.id).first()
                # print("Thank you for your submission. Here is the information we received:")
                # print(new_db_pet)
                add_new_pet(session, name, age, breed, temperament, treats, notes, owner_id)
                another = input("""
Would you like to add another pet? Yes/No: """).lower()
                if another == "no":
                    print("Routing you back to the main menu...")
                    add = False

        elif option == "update":
            # SAM - Write your code here! :-)
            print("You're updating a pet!")

        elif option == "remove":
                # print('removing pet...')
            # TERRENCE - Write your code here! :-)
            remove = True
            while remove:
                print('')
                pet_idx = int(input("Please Provide The 'Pet ID' Of The Pet You Wish To Remove: "))
                pets = session.query(Pet).filter(Pet.id == pet_idx).first()

                print('')
                print(pets)

                yes_no = input("Do You Wish To Delete This Pet? (Y/n)")
                if yes_no.lower() in YES:
                    session.delete(pets)
                    session.commit()
                    print('Your Pet Has been Removed Successfully!')
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





    # print('Hello! Welcome to the Wagging Rights CLI!')
    # print('Here is a list of available services:')
    # stores = session.query(Store)
    # create_store_table(stores)

    # # Get a choice of store, retrieve an object from the DB
    # store= None
    # while not store:
    #     store_id = input('Please enter the ID of the service that you wish to select: ')
    #     store = session.query(Store).filter(Store.id == store_id).one_or_none()

    # # Display list of items at the store
    # print('Here is a list of our services:')
    # create_service_item_table(store)

    # # Start adding items to cart
    # shopping_cart, cart_total = fill_cart(session, store)
    # print('Here are the services in your cart:')
    # show_cart(shopping_cart)

    # # Remove unwatned items from cart
    # remove_from_cart(session, shopping_cart, cart_total)

    # #Collect payment
    # print(f'Your total is ${cart_total:.2f}\n')
    # collect_payment(cart_total)

    # print('Thank you for using the Wagging Rights CLI!\n ')