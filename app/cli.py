#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Owner, Pet, Provider, Service

from helpers import update_pet, print_pet, add_new_pet, query_pets, book_house_sitting

from datetime import datetime

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
        pet_menu = True
        while pet_menu:
            print('')
            print('')
            print("Your Pet(s) Profile:")
            print('')

        # Use owner_id to query Pets table and return all pets associated with that owner.
            query_pets(session, owner_id)
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
                        continue

            elif option == "update":
                update = True
                while update: 
                    pet_id = int(input("You've selected update! Enter the ID of the pet you want to update: "))
                    pet = session.query(Pet).filter(Pet.id == pet_id, Pet.owner_id == owner_id).first()
                    if not pet:
                        print("Invalid ID. Please enter a valid ID that belongs to your pet.")
                        continue
                    else:
                        field = input(f"What updates would you like to make for {pet.name}? Enter 'name', 'age', 'breed', 'temperament', 'treats', or 'notes' to make those changes to {pet.name}'s record: ").lower()
                        if field not in ['name', 'age', 'breed', 'temperament', 'treats', 'notes']:
                            print("Invalid field. Please enter a valid field.")
                            continue
                        else:
                            new_value = input(f"Enter the new value for {field}: ")
                            update_pet(session, pet, field, new_value)
                            print_pet(pet)

                            another = input("Would you like to update another pet? Yes/No: ").lower()
                            if another == "no":
                                print("Routing you back to the main menu...")
                                update = False
                                continue

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
                            continue

                    else:
                        print('Pet has not been deleted.')

                        #NEED TO MAKE REMOVE OPTION SO THAT USERS CAN DELETE THEIR OWN PETS ONLY AND NOT OTHER USERS PETS.
                        #Run python seeds.py to restore table data

            else:
                print("Invalid input.")


    elif task == "appointment":
        # appointment_menu = True
        # while appointment_menu:
        print('')
        print('')
        print("Your Upcoming Bookings:")
        print('')

    query = session.query(Pet.id).filter(Pet.owner_id == owner_id).all()
    pet_ids = [pet[0] for pet in query]
    print(pet_ids)
    appointments = session.query(Service).filter(Service.pet_id.in_(pet_ids)).all()
    print(appointments)
    # for appointment in appointments:
    #     print(appointment)
    # TODO - We will reformat this printout later.
    request = input("""
PLEASE ENTER:
new - Request A New Appointment
cancel - Cancel An Appointment
view - View A List Of Our Providers

ENTER: """).lower()
    if request == "new":
        print('')
        print("Which pet are you scheduling this appointment for?")
        print('')
        query_pets(session, owner_id)
        id = int(input("Enter ID Of Pet You Would Like To Schedule For: "))

        name = session.query(Pet.name).filter(Pet.id == id).first()[0]

        appt_type = int(input(f"""What Type Of Appointment Are You Scheduling for {name}? 
PLEASE ENTER: 
1 - Drop-in, 
2 - Walking, 
3 - House-sitting

ENTER: """))
        
        if appt_type == 1:
            #drop-in code here
            pass

        elif appt_type == 2:
            #walking code here
            pass

        elif appt_type == 3:
            print("You Selected House-Sitting, which costs $70 per day.")
            start_date_str = input("""What Date Would You Like This Service To Start? 
Please Enter In MM/DD/YYYY Format: """)
                                   
            print(f"You've selected to book house-sitting beginning {start_date_str}.")

            end_date_str = input("""What Date Would You Like This Service To End? 
Please Enter In MM/DD/YYYY Format: """)
                                 
            print(f"You've selected to book house-sitting through {end_date_str}.")

            start_date = datetime.strptime(start_date_str, "%m/%d/%Y").date()
            end_date = datetime.strptime(end_date_str, "%m/%d/%Y").date()

            notes = input("Please Enter Any Notes For This Service Request: ")

            book_house_sitting(session, id, start_date, end_date, notes)

            next = input("Would You Like To Schedule Another Appointment? Y/N: ")
            print("Routing You Back To The Main Menu...")

        else:
            print("Please Enter A Valid Input.")


        


    
    elif request == "cancel":
        pass

    elif request == "view":
        pass

    else:
        print("Invalid input.")
        
# else:

#     print("Invalid input.")

    # print('Thank you for using the Wagging Rights CLI!\n ')
    # Add loop for pet menu.

