
print (''' 
                                           
                        |   | .    |   |  _ _   _ _            | | |      
                        |---| |    |   | |_ _  |_ _| |/        | | |
                        |   | |    |_ _|  _ _| |_ _  |         . . .     ''')
print ('''   
                _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
               |                               Items                             |
               |-----------------------------------------------------------------|
               |   Code  |         Item        |   Price   |   Quantity/Colour   |
               |---------|---------------------|-----------|---------------------|
               |  01     | Crayons             | 10.00 Dhs | 12 pcs / 12 colours |
               |  02     | White Board Marker  | 13.00 Dhs | 4 pcs / 4 colours   |
               |  03     | Ball Pen (Blue)     | 04.00 Dhs | 1 pcs / Blue colour | 
               |  04     | Ball Pen (Black)    | 04.00 Dhs | 1 pcs/Black colour  |
               |  05     | Sticky Notes        | 20.00 Dhs | 50 sheets/Neon color|
               |  06     | Pencil (12 / Black) | 06.00 Dhs | 12 pcs / Black color|
               |  07     | Sharpner w/ Eraser  | 05.00 Dhs | 1 pcs / with Eraser |
               |_ _ _ _ _|_ _ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _ _|
                                                                                          ''')

items = [{'Item_Code':'01',  'Item_Name':'Crayons (12 pcs)',            'Price':'10.00'},
         {'Item_Code':'02',  'Item_Name':'White Board Marker (4 pcs)',  'Price':'13.00'},
         {'Item_Code':'03',  'Item_Name':'Ball Pen (Blue)',             'Price':'04.00'},
         {'Item_Code':'04',  'Item_Name':'Ball Pen (Black)',            'Price':'04.00'},
         {'Item_Code':'05',  'Item_Name':'Sticky Notes (50 sheets)',    'Price':'20.00'},
         {'Item_Code':'06',  'Item_Name':'Pencil HB (12pcs/Black)',     'Price':'06.00'},
         {'Item_Code':'07',  'Item_Name':'Sharpner w/ Eraser',          'Price':'05.00'}]

print(" ")
print("~~~~~~~~~~~~~~~~~~~~ Welcome to the World Famous Vending Machine ~~~~~~~~~~~~~~~~~~~~")

is_quit = False
total_cost = 0  # Track the total cost of items
purchased_items = []  # List to store purchased items

while not is_quit:
    print("                                                                                     ")

    query = input("Enter the code number of the item you want to get (or type 'q' to quit): ")
    
    if query == 'q':
        is_quit = True
    else:
        item = next((i for i in items if i['Item_Code'] == query), None)

        if item is None:
            print('INVALID CODE')
        else:
            print(f"Great, {item['Item_Name']} will cost you {item['Price']} Dirhams")

            price = input(f"Enter the price of the product given on the menu: ")
            
            if price == item['Price']:
                total_cost += float(item['Price'])
                purchased_items.append(item)
                print(f"Thank you for buying.. Here is your {item['Item_Name']}!!!")
            else:
                print(f"Please enter only {item['Price']} Dirhams")

    another_item = input("Do you want to buy another item? (yes/no): ")
    if another_item.lower() != 'yes':
        is_quit = True

# Print the bill for all purchased items
print("\n\n--------------------- Your Bill ---------------------")
for item in purchased_items:
    print(f"Item Name: {item['Item_Name']} - Price: {item['Price']} Dirhams")

print(f"\nTotal cost of your purchase is: {total_cost} Dirhams")

# Ask for payment and calculate then display the balance
payment = input("Enter the payment amount: ")
if float(payment) >= total_cost:
    balance = float(payment) - total_cost
    print(f"Paid: {payment} Dirhams")
    print(f"Total cost of your purchase is: {total_cost} Dirhams")
    print(f"Balance: {balance} Dirhams")
else:
    print("Insufficient payment. Please pay the correct amount.")

print('''
                                        _ _ _
            \    / .  _ _  .  |        |     |  _ _   _ _   .  _ _        | | |
             \  /  | |_ _  | -|-       |-----| |   | |   |  | |   |       | | |
              \/   |  _ _| |  |_       |     | |_ _| |_ _|_ | |   |       . . . 
                                                   |
                                                _ _|
                                                                                       ''')

