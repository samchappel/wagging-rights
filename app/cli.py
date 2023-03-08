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
        pets = session.query(Pet).filter(Pet.owner_id == owner_id).all()
        for pet in pets:
            print(pet)
        # TODO - We will reformat this printout later.


    else:
        print("Yay, you chose 'appointments'! This feature is coming soon.")

    # Use owner_id to query Pets table and return all pets associated with that owner.

    # Prompt user to select from options to Add Pet, Update Pet, Remove Pet



    

    

