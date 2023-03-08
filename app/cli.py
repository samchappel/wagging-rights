#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from models import Store
# from helpers import (create_store_table, create_wagging_rights_item_table, fill_cart, show_cart, remove_from_cart, collect_payment)

engine = create_engine('sqlite:///wagging_rights.db')
session = sessionmaker(bind=engine)()


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