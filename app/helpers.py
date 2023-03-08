from models import Pet
# import click

def add_new_pet(session, name, age, breed, temperament, treats, notes, owner_id):
    new_pet = Pet(name=name, age=age, breed=breed, temperament=temperament, 
                favorite_treats=treats, notes=notes, owner_id=owner_id)
    session.add(new_pet)
    session.commit()
    new_db_pet = session.query(Pet).filter(Pet.id == new_pet.id).first()
    print('')
    print('')
    print("Thank You For Your Submission!")
    print('')
    print(new_db_pet)
    print("Your Pet Has Been Added Successfully!")




# def remove_pet(session, idx):


                # session.show(pet)
                # print('Do You Still Wish To Remove?')
                # new_db_pet = session.query(Pet).filter(Pet.id == id).first()
                # print('')
                # print('')
                # print('Thank You For Your Submission!')
                # print('')
                # print(new_db_pet)
                # print('Your Pet Has Been Removed Successfully!')



# from models import Service

# YES = ['y', 'ye', 'yes']
# NO = ['n', 'no']

# def create_request_table(requests):
#     print('-' * 50)
#     print(f'|ID |NAME{" " * 39}|')
#     print('-' * 50)
#     for request in requests:
#         id_spaces = 4 - len(str(request.id))
#         name_spaces = 43 - len(request.name)
#         print(f'|{request.id}{" " * id_spaces}|{request.name}{" " * name_spaces}|')
#     print('-' * 50)

# def create_item_table(request):
#     print('-' * 50)
#     print(f'|ID  |ITEM NAME{" " * 24}|PRICE{" " * 4}|')
#     print('-' * 50)
#     for item in sorted(request.items, key=lambda g: g.id):
#         id_spaces = 4 - len(str(item.id))
#         name_spaces = 33 - len(item.name)
#         price_spaces = 8 - len(f'{item.price:.2f}')
#         output_string = f'|{item.id}{" " * id_spaces}|' + \
#             f'{item.name}{" " * name_spaces}|' + \
#             f'${item.price:.2f}{" " * price_spaces}|'
#         print(output_string)
#     print('-' * 50)

# def fill_cart(session, request):
#     shopping_cart = ShoppingCart(request=request)
#     item_id = input('Please enter the ID of your first item: ')
#     cart_total = 0
#     while item_id:
#         item = session.query(Service).filter(
#             Service.id==item_id).first()
#         if item in request.items:
#             shopping_cart.items.append(item)
#             cart_total += item.price
#             print(f'Cart total is now ${cart_total:.2f}\n')
#         else:
#             item_id = input('Please enter a valid service item ID: ')
#             continue