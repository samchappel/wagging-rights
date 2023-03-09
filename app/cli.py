#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Owner, Pet, Provider, Service

from helpers import update_pet, print_pet, add_new_pet

engine = create_engine('sqlite:///wagging_rights.db')
session = sessionmaker(bind=engine)()

YES = ['y', 'ye', 'yes']
NO = ['n','no']
line = '-'*50
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
    owner_id = int(input(f"""Please Enter Your Owner Id To Get Started:

ENTER: """))

    # Use owner_id to query Owners table and return owner name.
    owner_name = session.query(Owner.name).filter(Owner.id == owner_id).first()[0].split(" ")[0]

    # Print Welcome, {Name} and prompt them to input whether they would like to manage pets or appointments.
    print('\n' + line + '\n')
    print(f"Welcome, {owner_name}! What Would You Like To Do Today?")
    print('')
    print(f'Please Enter:')
    main_menu = True
    while main_menu:
        task = input(f"""
    pet - View Your Pet Profile(s)
    appointment - Book An Appointment

ENTER: """).lower()

    # If 'Pets' bring user to 'Pet Menu' pets.
        if task == "pet":
            pet_menu = True
            while pet_menu:
                print('')
                print('-'*50)
                print('')
                print("Your Pet Profile(s):")
                print('')

            # Use owner_id to query Pets table and return all pets associated with that owner.
                pets = session.query(Pet).filter(Pet.owner_id == owner_id).all()
                for pet in pets:
                    print(pet)
                # TODO - We will reformat this printout later.

            # Prompt user to select from options to Add Pet, Update Pet, Remove Pet
                option = input("""Please Enter:

    add - Add A Pet
    update - Update A Pet
    remove - Remove A Pet
    back - return to Task Menu

ENTER: """).lower()

                if option == "add":
                    add = True
                    while add:
                        print('')
                        print('')
                        print("Please Provide Information About Your New Pet!")
                        print('-'*50)
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
                        print('-'*50)
                        pet_id = int(input(f"""You've Selected Update! Enter The ID Of The Pet You Want To Update:

ENTER: """))
                        pet = session.query(Pet).filter(Pet.id == pet_id, Pet.owner_id == owner_id).first()
                        if not pet:
                            print(f"""Invalid ID. Please enter a valid ID that belongs to your pet.

ENTER: """)
                            continue
                        else:
                            print('')
                            field = input(f"""What updates would you like to make for {pet.name}? Enter 'name', 'age', 'breed', 'temperament', 'treats', or 'notes' to make those changes to {pet.name}'s record:

ENTER: """).lower()
                            if field not in ['name', 'age', 'breed', 'temperament', 'treats', 'notes']:
                                print(f"""Invalid field. Please enter a valid field.""")
                                continue
                            else:
                                new_value = input(f"""Enter the new value for {field}:

ENTER: """)
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
                        pet_idx = int(input(f"""Please Provide A Valid 'Pet ID' Of The Pet You Wish To Remove:

ENTER: """))
                        pets = session.query(Pet).filter(Pet.id == pet_idx).first()
                        if pets.owner_id == owner_id:
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
                                    pet_menu = False
                                else:
                                    print('')
                                    print('ERROR: Please select a valid Pet ID.')
                                    continue
                    else:
                        print('')
                        print('ERROR: Please select a valid Pet ID.')
                        continue

                elif option == 'back':
                    pet_menu = False



                else:
                    print("Invalid input.")


        elif task == "appointment":
            appointment_menu = True
            while appointment_menu:
                print('')
                print('-'*50)
                print('')
                print("Your Pets With Upcoming Bookings:")
                print('')

                query = session.query(Pet).filter(Pet.owner_id == owner_id).all()
                pets = [pet for pet in query]
                for pet in pets:
                    print(pet.name)
                print(f'-'*50)
                print('')
                print(f'Appointment(s): ')
                for pet in pets:
                    services = session.query(Service).filter(Service.pet_id == pet.id).all()
                    for service in services:
                        if service.pet_id == pet.id:
                            print('')
                            print(service)
                            print('-'*50)
#     print(f"""
#     ID: {service.id}
#     Request: {service.request}
#     Start Date: {service.start_date}
#     End Date :{service.end_date}
#     Fee: {service.fee}
#     Notes: {service.notes}
# {line}
#     """)
    # for appointment in appointments:
    #     print(appointment)
    # TODO - We will reformat this printout later.
                request = input("""
Please Enter:

    new - Request A New Appointment
    cancel - Cancel An Appointment
    view - View A List Of Our Providers
    back - Go Back To Main Menu

ENTER: """).lower()
                if request == "new":
                    pass

                elif request == "cancel":
                    cancel = True
                    while cancel:
                        print('')
                        service_idx = int(input(f"""Please Provide The 'Service ID' Of The Service You Wish To Cancel:

ENTER: """))
                        service = session.query(Service).filter(Service.id == service_idx).first()
                        print('')
                        print('-'*50)
                        print('')
                        print(service)
                        print('-'*50)
                        print('')

        # print(service)
                        yes_no = input("Do You Wish To Cancel This Service? (Y/n): ")
                        if yes_no.lower() in YES:
                            session.delete(service)
                            session.commit()
                            print('')
                            print('-'*50)
                            print('')
                            print('Your Service Has been Removed Successfully!')
                            print('')
                            rem_another = input(f'''Would You Like To Remove Another Service? (Y/n):

ENTER: ''')
                            if rem_another.lower() in YES:
                                continue
                            elif rem_another.lower() in NO:
                                print("Routing you back to Appointment Menu...")
                                cancel = False
                                appointment_menu = True
                            else:
                                print("Invalid input. Routing you back to main menu...")
                                cancel = False
                                appointment_menu = False

                                continue

                elif request == "view":
                    view = True
                    while view:
                        print('')
                        providers = session.query(Provider).all()
                        print('-'*50)
                        print("Available Providers:")
                        print('')
                        for provider in providers:
                            print(f"Provider ID: {provider.id} | Provider Name: {provider.name} | Provider Email: {provider.email}")
                            print('')
                        back = input('Would You Like To Return To Appointment Menu? (Y/n): \n')
                        if back.lower() in YES:
                            view = False

                elif request == "back":
                    appointment_menu = False

                else:
                    print("Invalid input.")

# else:

#     print("Invalid input.")

    # print('Thank you for using the Wagging Rights CLI!\n ')
    # Add loop for pet menu.

