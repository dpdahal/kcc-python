print("=============Computer Bazar=======")
print("1.Dell(Rs:2000) 2. Toshiba(Rs:30000) 3.Mac(Rs:50000)")
option = int(input("Select any option: "))
dell_price = 0
toshiba_price = 0
mac_price = 0
quantity = 0
select_option = ''

if option == 1:
    quantity = int(input("Enter quantity: "))
    dell_price += 20000 * quantity
    select_option = 'Dell'

elif option == 2:
    quantity = int(input("Enter quantity: "))
    toshiba_price += 30000 * quantity
    select_option = 'Toshiba'
elif option == 3:
    quantity = int(input("Enter quantity: "))
    mac_price += 50000 * quantity
    select_option = 'Mac'
else:
    print("Invalid option")
    exit()

print("Delivery: 1. Home(Rs: 1000) 2. Pickup(Free)")

delivery_option = int(input("Enter option: "))
delivery_price = 0

if delivery_option == 1:
    delivery_price += 1000

print("Packing: 1. Plastic(Rs: 500) 2. Bag(Rs:1000) 3. Gift Box(Rs:5000) 4. None")
plastic_price = 0
bag_price = 0
gif_box_price = 0

packing_option = int(input("Enter option: "))
if packing_option == 1:
    plastic_price += 500

elif packing_option == 2:
    bag_price += 1000

elif packing_option == 3:
    gif_box_price += 5000

total = dell_price + mac_price + toshiba_price
print("Location: 1.KTM(13% tax) 2. BKT(free) 3.(Free)")
location_option = int(input("Enter option: "))
tax_amount = 0

if location_option == 1:
    tax_amount += total * 0.13

gt = total + tax_amount + delivery_price + plastic_price + bag_price + gif_box_price

print("=======Bill============")
print(f"Product name: {select_option}")
print(f"Total Quantity: {quantity}")
print(f"Tax Amt: {tax_amount}")
print(f"GT : {gt}")
