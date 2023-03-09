#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime
import colorama

from models import Owner, Pet, Provider, Service

from helpers import update_pet, print_pet, add_new_pet, query_pets, create_new_dropwalk, book_house_sitting, check_id

engine = create_engine('sqlite:///wagging_rights.db')
session = sessionmaker(bind=engine)()

YES = ['y', 'ye', 'yes']
NO = ['n','no']
line = '-'*50 #adds line
line_db = '\n' + line + '\n' #adds line with double spacing


if __name__ == '__main__':
    #Intro: welcome to the CLI, pick a store


    colorama.init()

    print(colorama.Fore.YELLOW +'''
██╗    ██╗ █████╗  ██████╗  ██████╗ ██╗███╗   ██╗ ██████╗ ██████╗ ██╗ ██████╗ ██╗  ██╗████████╗███████╗
██║    ██║██╔══██╗██╔════╝ ██╔════╝ ██║████╗  ██║██╔════╝ ██╔══██╗██║██╔════╝ ██║  ██║╚══██╔══╝██╔════╝
██║ █╗ ██║███████║██║  ███╗██║  ███╗██║██╔██╗ ██║██║  ███╗██████╔╝██║██║  ███╗███████║   ██║   ███████╗
██║███╗██║██╔══██║██║   ██║██║   ██║██║██║╚██╗██║██║   ██║██╔══██╗██║██║   ██║██╔══██║   ██║   ╚════██║
╚███╔███╔╝██║  ██║╚██████╔╝╚██████╔╝██║██║ ╚████║╚██████╔╝██║  ██║██║╚██████╔╝██║  ██║   ██║   ███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝

                                        |\_/|
                                        | @ @   Woof!
                                        |   <>              _
                                        |  _/\------____ ((| |))
                                        |               `--' |
                                    ____|_       ___|   |___.'
                                    /_/_____/____/_______|

''' + colorama.Style.RESET_ALL)

    print("Welcome To Wagging Rights CLI!")
    print('')
    # Ask user to input their ID number (corresponds with owner_id)

# NEW - Bianca - Add error-handling for owner_id input.
    log_in = True
    while log_in:
        try:
            owner_id = int(input(f"""Please Enter Your Owner Id To Get Started:

ENTER: """))
            valid_owner_id = check_id(session, Owner, owner_id)
            if valid_owner_id:
                log_in = False
            else:
                print("Invalid ID. Please try again.")
        except ValueError:
            print("Invalid ID. Please try again.")
# END - Bianca - error-handling for owner_id input.

    # Use owner_id to query Owners table and return owner name.
    owner_name = session.query(Owner.name).filter(Owner.id == owner_id).first()[0].split(" ")[0]
    # Print Welcome, {Name} and prompt them to input whether they would like to manage pets or appointments.
    print('\n' + line + '\n')
    print(f"Welcome, {owner_name}! What Would You Like To Do Today?")
    print('')
    print(f'Please Enter:')


#MAIN MENU" START:
    main_menu = True
    while main_menu:
        task = input(f"""
    pet - View Your Pet Profile(s)
    appointment - Book An Appointment

ENTER: """).lower()

#"PET MENU" START:
        if task == "pet":
            pet_menu = True
            while pet_menu:
                print('\n' + line + '\n')
                print("Your Pet Profile(s):")
                print('')
                # Use owner_id to query Pets table and return all pets associated with that owner.
                pets = session.query(Pet).filter(Pet.owner_id == owner_id).all()
                for pet in pets:
                    print(pet)
                # Prompt user to select from options to Add Pet, Update Pet, Remove Pet
                option = input("""Please Enter:

    add - Add A Pet
    update - Update A Pet
    remove - Remove A Pet
    back - return to Task Menu

ENTER: """).lower()

#"ADD OPTION" START:
                if option == "add":
                    add = True
                    while add:
                        print('\n' +'\n')
                        print('')
                        print("Please Provide Information About Your New Pet!")
                        print(line)
                        print('')
                        name = input("Name: ")
                        age = int(input("Age: "))
                        breed = input("Breed: ")
                        temperament = input("Temperament: ")
                        treats = input("Favorite Treats: ")
                        notes = input("Additional Notes/Special Needs: ")
                        add_new_pet(session, name, age, breed, temperament, treats, notes, owner_id)
                        yes_no = input("""
Would you like to add another pet? Yes/No: """).lower()
                        if yes_no.lower() in YES:
                            continue
                        elif yes_no.lower() in NO:
                            print("Routing you back to the main menu...")
                            add = False
                            continue
#"ADD OPTION" END.


#"UPDATE OPTION" START:
                elif option == "update":
                    update = True
                    while update:
                        print(line)
    # NEW - Bianca - Error-handling for invalid pet ids.
                        pet_selection = True
                        while pet_selection:
                            try:
                                pet_id = int(input(f"""You've Selected Update! Enter The ID Of The Pet You Want To Update:

ENTER: """))
                                pet_selection = False
                            except ValueError:
                                print("Invalid ID. Please try again.")
    # END - Bianca - Error-handling for invalid pet ids.

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
                                yes_no = input("Would you like to update another pet? Yes/No: ").lower()
                                if yes_no.lower() in YES:
                                    continue
                                elif yes_no.lower() in NO:
                                    print("Routing you back to the main menu...")
                                    update = False

#"UPDATE OPTION" END.


#"REMOVE OPTION" START:
                elif option == "remove":
                    remove = True
                    while remove:
                        print('')
    # NEW - Bianca - Add error-handling for invalid pet_id.
                        pet_selection = True
                        while pet_selection:
                            try:
                                pet_idx = int(input(f"""Please Provide A Valid 'Pet ID' Of The Pet You Wish To Remove:

ENTER: """))
                                pet_selection = False
                            except ValueError:
                                print("Invalid ID. Please try again.")
    # END - Bianca - Add error-handling for invalid pet_id.
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
                                else:
                                    print('')
                                    print('ERROR: Please select a valid Pet ID.')
                                    continue
                    else:
                        print('')
                        print('ERROR: Please select a valid Pet ID.')
                        continue
#"REMOVE OPTION" END.


#"BACK OPTION" START:
                elif option == 'back':
                    pet_menu = False
#"BACK OPTION" END.


                else:
                    print("Invalid input.")
#"PET MENU" END.





#"APPOINTMENT MENU" START:
        elif task == "appointment":
            appointment_menu = True
            while appointment_menu:
                print(line_db)
                print("Your Pets With Upcoming Bookings:")
                print(line_db)
                query = session.query(Pet).filter(Pet.owner_id == owner_id).all()
                pets = [pet for pet in query]
                for pet in pets:
                    print(pet.name)
                print(f'Appointment(s): ')
                for pet in pets:
                    services = session.query(Service).filter(Service.pet_id == pet.id).all()
                    for service in services:
                        if service.pet_id == pet.id:
                            print('')
                            print(service)
                            print(line)
                request = input("""
Please Enter:

    new - Request A New Appointment
    cancel - Cancel An Appointment
    view - View A List Of Our Providers
    back - Go Back To Main Menu

ENTER: """).lower()
# NEW REQUEST START

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

                    fees = {"Drop-In": 50, "Walking": 35, "House-Sitting": 70}

                    if appt_type == 1 or appt_type == 2:

                        if appt_type == 1:
                            service = "Drop-In"

                        elif appt_type == 2:
                            service = "Walking"

                        print(f"You selected {service}, which costs ${fees[service]}.00 per session.")

                        date_input = input("""
What date would you like to schedule this service for?
Enter using MM/DD/YYYY format

ENTER: """)

                        print(f"You selected {date_input} for your service date.")

                        time_input = input("""
This service can be scheduled between the hours of 8:00 AM and 5:00 PM.
What time would you like to schedule this service for?
Enter using HH:MM format (do not include 'AM' or 'PM')

ENTER: """) + ":00"

                        print(f"You selected {time_input} as your start time for this service.")

                        formatter = "%m/%d/%Y %H:%M:%S"

                        string_datetime = f"{date_input} {time_input}"

                        formatted_datetime = datetime.strptime(string_datetime, formatter)

                        add_note = input("Please Enter Any Notes For This Service Request: ")

                        create_new_dropwalk(session=session, pet_id=id, request=service, start_date=formatted_datetime, fee=f"${fees[service]}.00", notes=add_note)

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
# NEW REQUEST END


#"CANCEL REQUEST" START:
                elif request == "cancel":
                    cancel = True
                    while cancel:
                        print('')
                        service_idx = int(input(f"""Please Provide The 'Service ID' Of The Service You Wish To Cancel:

ENTER: """))
                        service = session.query(Service).filter(Service.id == service_idx).first()
                        print(line_db)
                        print(service)
                        print(line)
                        print('')
                        yes_no = input("Do You Wish To Cancel This Service? (Y/n): ")
                        if yes_no.lower() in YES:
                            session.delete(service)
                            session.commit()
                            print(line_db)
                            print('Your Service Has been Removed Successfully!')
                            print('')
                            rem_another = input(f'''Would You Like To Remove Another Service? (Y/n):

ENTER: ''')
                            if rem_another.lower() in YES:
                                continue
                            elif rem_another.lower() in NO:
                                print("Routing You Back To Appointment Menu...")
                                cancel = False
                                appointment_menu = True
                        elif yes_no.lower() in NO:
                            print("Routing You Back To Appointment Menu...")
                            cancel = False
                            appointment_menu = False
                            continue
#"CANCEL REQUEST" END.


#"VIEW PROVIDERS" START:
                elif request == "view":
                    view = True
                    while view:
                        print('')
                        providers = session.query(Provider).all()
                        print('-'*50)
                        print('')
                        print("Available Providers:")
                        print('')
                        for provider in providers:
                            print(f"Provider ID: {provider.id} | Provider Name: {provider.name} | Provider Email: {provider.email}")
                            print('')
                        back = input('Would You Like To Return To Appointment Menu? (Y/n): \n')
                        if back.lower() in YES:
                            view = False
#"VIEW PROVIDERS" END

#GO BACK
                elif request == "back":
                    appointment_menu = False

#If Invalid Input
        else:
            print("Please Enter A Valid Input.")

    # print('Thank you for using the Wagging Rights CLI!\n ')
    # Add loop for pet menu.

