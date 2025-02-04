
print (''' 
                                           
                        |   | .    |   |  _ _   _ _            | | |      
                        |---| |    |   | |_ _  |_ _| |/        | | |
                        |   | |    |_ _|  _ _| |_ _  |         . . .     ''')
print ('''   
                _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
               |                          Medicines                          |
               |-------------------------------------------------------------|
               |   Code  |        Item       |   Price   |      Used For     |
               |---------|-------------------|-----------|-------------------|
               |  01     | Antiseptic pads   | 15.00 Dhs | Cleansing wounds  |
               |  02     | Medical tape      | 05.00 Dhs | Dressings wounds  |
               |  03     | Elastic bandages  | 08.00 Dhs | Dressings wounds  |
               |  04     | Hand sanitizer    | 11.00 Dhs | Disinfectants     |
               |  05     | Sterile gloves    | 06.00 Dhs | Protection        |
               |  06     | ORS (Orange)      | 03.00 Dhs | Treat dehydration |
               |  07     | Water             | 02.00 Dhs | Treat dehydration |
               |_ _ _ _ _|_ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _|_ _ _ _ _ _ _ _ _ _|
                                                                                 ''')

items = [{'Item_Code':'01',  'Item_Name':'Antiseptic pads',           'Price':'15.00'},
         {'Item_Code':'02',  'Item_Name':'Medical tape',              'Price':'05.00'},
         {'Item_Code':'03',  'Item_Name':'Elastic bandages',          'Price':'08.00'},
         {'Item_Code':'04',  'Item_Name':'Hand sanitizer',            'Price':'11.00'},
         {'Item_Code':'05',  'Item_Name':'Sterile gloves',            'Price':'06.00'},
         {'Item_Code':'06',  'Item_Name':'Oral Rehydration Solution', 'Price':'03.00'},
         {'Item_Code':'07',  'Item_Name':'Water',                     'Price':'02.00'}]

print(" ")
print("~~~~~~~~~~~~~~~~~~~~ Welcome to the World Famous Vending Machine ~~~~~~~~~~~~~~~~~~~~")

is_quit = False
total_cost = 0                      # Track the total cost of items
purchased_items = []                # List to store purchased items

while not is_quit:
    print("                  ")

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
            _ _ _                                       _ _ _
           |        _ _   |       |    |  _ _  | |     |        _ _   _ _   _ _      | | |
           |   --  |_ _| -|-      | /\ | |_ _| | |     |-----| |   | |   | |   |     | | |
           |_ _ _| |_ _   |_      |/  \| |_ _  | |      _ _ _| |_ _| |_ _| |   |     . . .
                                                                                               ''')
