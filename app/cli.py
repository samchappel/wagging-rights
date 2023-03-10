#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime
from models import Owner, Pet, Provider, Service

import colorama
import pandas as pd

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

    print("Welcome to Wagging Rights CLI!")
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
    print(f"Welcome, {owner_name}! What would you like to do today?")
    print('')
    print(f'Please Enter:')


#MAIN MENU" START:
    main_menu = True
    while main_menu:
        task_selection = True
        while task_selection:
            try:
                task = int(input(f"""
    1 - View Your Pet Profile(s)
    2 - Book An Appointment

ENTER: """))
                if task in [1, 2]:
                    task_selection = False
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid selection. Please try again.")


#"PET MENU" START:
        if task == 1:
            pet_menu = True
            while pet_menu:
                print('\n' + line + '\n')
                print("Your Pet Profile(s):")
                print('')
                # Use owner_id to query Pets table and return all pets associated with that owner.
                pets = session.query(Pet).filter(Pet.owner_id == owner_id).all()
                for pet in pets:
                    pet_table = pd.Series([pet.id,pet.name,pet.age,pet.breed,pet.temperament,pet.favorite_treats,pet.notes,pet.owner_id], index=['Pet ID','Pet Name','Pet Age','Pet Breed','Pet Temperament','Pet Treats','Pet Notes','Pet Owner ID'])
                    print(pet_table.to_string() + '\n' +line)
                # Prompt user to select from options to Add Pet, Update Pet, Remove Pet
                pet_menu_selection = True
                while pet_menu_selection:
                    try:
                        option = int(input("""Please Enter:

    1 - Add A Pet
    2 - Update A Pet
    3 - Remove A Pet
    4 - Return To Task Menu

ENTER: """))
                        if option in [1, 2, 3, 4]:
                            pet_menu_selection = False
                        else:
                            print("Invalid selection. Please try again.")
                    except ValueError:
                        print("Invalid selection. Please try again.")

#"ADD OPTION" START:
                if option == 1:
                    add = True
                    while add:
                        print('\n' +'\n')
                        print('')
                        print("Please provide information about your new pet!")
                        print(line)
                        print('')
#work: lines 105-110 use pandas
                        name = input("Name: ")
    # NEW - Bianca - Add error handling for age input.
                        age_input = True
                        while age_input:
                            try:
                                age = int(input("Age: "))
                                age_input = False
                            except ValueError:
                                print("Invalid selection. Please try again.")
    # END - Bianca - Add error handling for age input.
                        breed = input("Breed: ")
                        temperament = input("Temperament: ")
                        treats = input("Favorite Treats: ")
                        notes = input("Additional Notes/Special Needs: ")
                        add_new_pet(session, name, age, breed, temperament, treats, notes, owner_id)
                        yes_no = input("""
Would you like to add another pet? Y/N: """).lower()
                        if yes_no.lower() in YES:
                            continue
                        elif yes_no.lower() in NO:
                            print("Routing you back to the main menu...")
                            add = False
                            continue
#"ADD OPTION" END.


#"UPDATE OPTION" START:
                elif option == 2:
                    update = True
                    while update:
                        print(line)

    # NEW - Bianca - Error-handling for invalid pet ids.
                        pet_selection = True
                        while pet_selection:
                            try:
                                pet_id = int(input(f"""You've selected update! Enter the ID of the pet you want to update or enter 0 to go back.

ENTER: """))
                                pet_selection = False
                            except ValueError:
                                print("Invalid ID. Please try again.")
    # END - Bianca - Error-handling for invalid pet ids.
                        if pet_id == 0:
                            update = False
                            continue
                        pet = session.query(Pet).filter(Pet.id == pet_id, Pet.owner_id == owner_id).first()
                        if not pet:
                            print(f"""Invalid ID. Please enter a valid ID that belongs to your pet or enter 0 to go back.

ENTER: """)
                            continue
                        else:
                            print('')
                            field = int(input(f"""What updates would you like to make for {pet.name}? 
1 - Name 
2 - Age 
3 - Breed 
4 - Temperament
5 - Treats
6 - Notes

ENTER: """))
                            fields = {1: "Name", 2: "Age", 3: "Breed", 4: "Temperament", 5: "Treats", 6: "Notes"}
                            new_value = input(f"""Enter the new value for {fields[field]}.

ENTER: """)
                            update_pet(session, pet, fields[field].lower(), new_value)
                            print_pet(pet)
                            yes_no = input("Would you like to update another pet? Yes/No: ").lower()
                            if yes_no.lower() in YES:
                                continue
                            elif yes_no.lower() in NO:
                                print("Routing you back to the main menu...")
                                update = False

#"UPDATE OPTION" END.


#"REMOVE OPTION" START:
                elif option == 3:
                    remove = True
                    while remove:
                        print('')

    # NEW - Bianca - Add error-handling for invalid pet_id.
                        pet_selection = True
                        while pet_selection:
                            try:
                                pet_idx = int(input(f"""Please provide a valid Pet ID of the pet you wish to remove or enter 0 to go back.

ENTER: """))
                                valid_pet_id = check_id(session, Pet, pet_idx)
                                if valid_pet_id or pet_idx == 0:
                                    pet_selection = False
                                else:
                                    print("Invalid ID. Please try again.")
                            except ValueError:
                                print("Invalid ID. Please try again.")
    # END - Bianca - Add error-handling for invalid pet_id.
                        if pet_idx == 0:
                            remove = False
                            continue
                        pets = session.query(Pet).filter(Pet.id == pet_idx).first()
                        #TERRENCENOTE: if no pets.owner_id matches with owner_id print "no pets to remove"
                        #return them back to pet_menu
                        if pets.owner_id == owner_id:
                            print('')
                            print(pets)
                            yes_no = input("Do you wish to delete this pet? (Y/N): \n")
                            if yes_no.lower() in YES:
                                session.delete(pets)
                                session.commit()
                                print('Your pet has been removed successfully!')
                                rem_another = input('Would you like to remove another pet? (Y/N): \n')
                                if rem_another.lower() in YES:
                                    continue
                                elif rem_another.lower() in NO:
                                    print("Routing you back to main menu...")
                                    remove = False
                                else:
                                    print('')
                                    print('ERROR: Please select a valid Pet ID.')
                                    continue
                    else: #TERRENCENOTE: I think lines 185-188 can be removed.
                        print('')
                        print('ERROR: Please select a valid Pet ID.')
                        continue
#"REMOVE OPTION" END.


#"BACK OPTION" START:

                elif option == 4:
                    pet_menu = False
#"BACK OPTION" END.


                else:
                    print("Invalid input.")
#"PET MENU" END.





#"APPOINTMENT MENU" START:
        elif task == 2:
            appointment_menu = True
            while appointment_menu:
                print(line_db)
                print("Your upcoming bookings:")
                print(line_db)
                query = session.query(Pet).filter(Pet.owner_id == owner_id).all()
                pets = [pet for pet in query]
                print(f'Appointment(s): ')
                for pet in pets:
                    services = session.query(Service).filter(Service.pet_id == pet.id).all()
                    for service in services:
                        if service.pet_id == pet.id:
                            # service_data = {'Service ID':[service.id], 'Request':[service.request], 'Start Date':[service.start_date], 'End Date':[service.end_date], 'Fee':[service.fee],'Notes':[service.notes]}
                            # service_df = pd.DataFrame(service_data, columns=['Service ID', 'Request','Start Date', 'End Date', 'Fee', 'Notes'])
                            appointment_table = pd.Series([service.id,service.request,service.start_date,service.end_date,service.fee,service.notes], index = ['Service ID','Service Request','Service Start Date','Service End Date','Service Fee','Service Notes'])
                            print('')
                            print(appointment_table.to_string())
                            print(line)

                request = int(input("""
Please Enter:

    1 - Request A New Appointment
    2 - Cancel An Appointment
    3 - View A List Of Our Providers
    4 - Go Back To Main Menu

ENTER: """))
# NEW REQUEST START

                if request == 1:
                    print('')
                    print("Which pet are you scheduling this appointment for?")
                    print('')
                    query_pets(session, owner_id)

    # NEW - Bianca - Error-handling for invalid pet ids.
                    pet_selection = True
                    while pet_selection:
                        try:
                            id = int(input("Enter ID Of Pet You Would Like To Schedule For: "))
                            valid_pet_id = check_id(session, Pet, id)
                            if valid_pet_id:
                                owners_pets = session.query(Pet.id).filter(Pet.owner_id == owner_id).all()
                                owners_pets_ids = [id[0] for id in owners_pets]
                                if id in owners_pets_ids:
                                    pet_selection = False
                                else:
                                    print("Invalid ID. Please try again.")
                            else:
                                print("Invalid ID. Please try again.")
                                
                        except ValueError:
                            print("Invalid ID. Please try again.")

    # END - Bianca - Error-handling for invalid pet ids.

                    name = session.query(Pet.name).filter(Pet.id == id).first()[0]

    # NEW - Bianca - Error-handling for invalid menu selection.
                    appt_selection = True
                    while appt_selection:
                        try:

                            appt_type = int(input(f"""What Type Of Appointment Are You Scheduling for {name}?

PLEASE ENTER:
1 - Drop-in
2 - Walking
3 - House-sitting

ENTER: """))
                            if appt_type in [1, 2, 3]:
                                appt_selection = False
                            else:
                                print("Invalid selection. Please try again.")
                        except ValueError:
                            print("Invalid selection. Please try again.")
    # END - Bianca - Error-handling for invalid menu selection.

                    fees = {"Drop-In": 50, "Walking": 35, "House-Sitting": 70}

                    if appt_type == 1 or appt_type == 2:

                        if appt_type == 1:
                            service = "Drop-In"

                        elif appt_type == 2:
                            service = "Walking"

                        print(f"You selected {service}, which costs ${fees[service]}.00 per session.")
    # NEW - Bianca - Add error handling for invalid date or time entry.
                        datetime_entry = True
                        while datetime_entry:
                            try:
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

                                print(f"Appointment Date/Time: {formatted_datetime}")
                                datetime_entry = False
                            except ValueError:
                                print("Something went wrong. Please try again.")
    # END - Bianca - Add error handling for invalid date or time entry.

                        add_note = input("Please enter any notes for this service request: ")

                        create_new_dropwalk(session=session, pet_id=id, request=service, start_date=formatted_datetime, fee=f"${fees[service]}.00", notes=add_note)

                    elif appt_type == 3:

    # NEW - Bianca - Add error-handling for invalid date/time entry.
                        datetime_entry = True
                        while datetime_entry:
                            try:
                                service = "House-Sitting"
                                print(f"You selected {service}, which costs ${fees[service]}.00 per session.")
                                start_date_str = input("""What date would you like this service to start?
Please Enter In MM/DD/YYYY Format: """)

                                print(f"You've selected to book house-sitting beginning {start_date_str}.")

                                end_date_str = input("""What date would you like this service to end?
Please Enter In MM/DD/YYYY Format: """)


                                print(f"You've selected to book house-sitting through {end_date_str}.")

                                start_date = datetime.strptime(start_date_str, "%m/%d/%Y").date()
                                end_date = datetime.strptime(end_date_str, "%m/%d/%Y").date()

                                print(f"Appointment Date/Time Selection - Start: {start_date}, End: {end_date}")
                                datetime_entry = False
                            except ValueError:
                                print("Something went wrong. Please try again.")
    # END - Bianca - Add error-handling for invalid date/time entry.

                        notes = input("Please Enter Any Notes For This Service Request: ")

                        book_house_sitting(session, id, start_date, end_date, notes)

                        next = input("Would you like to schedule another appointment? Y/N: ")
                        print("Routing you back to the main menu...")

                    else:
                        print("Please enter a valid input.")
# NEW REQUEST END


#"CANCEL REQUEST" START:
                elif request == 2:
                    cancel = True
                    while cancel:
                        print('')

    # NEW - Bianca - Error-handling for invalid menu selection.
                        service_selection = True
                        while service_selection:
                            try:
                                service_idx = int(input(f"""Please provide the Service ID of the service you wish to cancel.


ENTER: """))
                                valid_service_id = check_id(session, Service, service_idx)
                                if valid_service_id:
                                    service_ids = []
                                    for service in services:
                                        if service.pet_id == pet.id:
                                            service_ids.append(service.id)
                                    if service_idx in service_ids:
                                        service_selection = False
                                    else:
                                        print("Invalid ID. Please try again.")
                                else:
                                    print("Invalid ID. Please try again.")
                            except ValueError:
                                print("Invalid ID. Please try again.")
    # END - Bianca - Error-handling for invalid menu selection.
                        service = session.query(Service).filter(Service.id == service_idx).first()
                        print(line_db)
                        print(service)
                        print(line)
                        print('')
                        yes_no = input("Do you wish to cancel this service? (Y/N): ")
                        if yes_no.lower() in YES:
                            session.delete(service)
                            session.commit()
                            print(line_db)
                            print('Your service has been removed successfully!')
                            print('')
                            rem_another = input(f'Would You like to remove another service? (Y/N): ')
                            if rem_another.lower() in YES:
                                continue
                            elif rem_another.lower() in NO:
                                print("Routing you back to appointment menu...")
                                cancel = False
                                appointment_menu = True
                        elif yes_no.lower() in NO:
                            print("Routing you back to appointment menu...")
                            cancel = False
                            appointment_menu = False
                            continue
#"CANCEL REQUEST" END.


#"VIEW PROVIDERS" START:
                elif request == 3:
                    view = True
                    while view:
                        print('')
                        providers = session.query(Provider).all()
                        print(line)
                        print('')
                        print("Available Providers:")
                        print('')
                        for provider in providers:
                            print(f"Provider ID: {provider.id} | Provider Name: {provider.name} | Provider Email: {provider.email}")
                            print('')
                        back = input('Would you like to return to appointment menu? (Y/N): \n')
                        if back.lower() in YES:
                            view = False
#"VIEW PROVIDERS" END

#GO BACK

                elif request == 4:
                    appointment_menu = False
                    continue

#If Invalid Input
        else:
            print("Please enter a valid input.")

    # print('Thank you for using the Wagging Rights CLI!\n ')
    # Add loop for pet menu.

