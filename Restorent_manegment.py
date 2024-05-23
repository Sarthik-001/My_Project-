print("\t\t\t\t\t-----------------------------------")
print("\t\t\t\t\t\tWelcome to my Restorent")
print("\t\t\t\t\t-----------------------------------")

Restorent_card = {
    "panipuri": 30, "dahipuri": 45, "alu chat": 35,
    "samosa": 15, "paneer tikka": 156, "tikka roll": 65,
    "veg crispy": 80, "dal rice": 120, "total thali": 150,
    "cornoto icecream":25, "fixfriute":45,"bisleri water":20
}

menu_list = [
    "panipuri", "dahipuri", "alu chat",
    "samosa", "paneer tikka", "tikka roll",
    "veg crispy", "dal rice", "total thali",
    "cornoto icecream","fixfriute","bisleri water"
]

print("1. panipuri rs.30\n2. dahipuri rs.45\n3. alu chat rs.35\n4. samosa rs.15\n5. paneer tikka rs.156\n6. tikka roll rs.65\n7. veg crispy rs.80\n8. dal rice rs.120\n9. total thali rs.150\n10. bisleri water\n11. fixfriute")

total_amount = 0
order_list = []

order_number = int(input("\nEnter the number of food: ")) - 1

if 0 <= order_number < len(menu_list):
    order = menu_list[order_number]
    quantity = int(input("Enter the quantity: "))
    total_amount += Restorent_card[order] * quantity
    order_list.append((order, quantity))
    print(f"Your item {order} (x{quantity}) has been added to your order list.")
else:
    print("Please order something from the menu.")

while True:
    ask_another_item = input("Do you like to add another item? yes/no: ").strip().lower()
    if ask_another_item == "yes":
        order_number = int(input("Enter the number of food: ")) - 1
        if 0 <= order_number < len(menu_list):
            order = menu_list[order_number]
            quantity = int(input("Enter the quantity: "))
            total_amount += Restorent_card[order] * quantity
            order_list.append((order, quantity))
            print(f"Your item {order} (x{quantity}) has been added to your order list.")
        else:
            print("Please order something from the menu.")
    else:
        break

print(f"Your total order is: {order_list}")
print(f"Your total amount is: Rs.{total_amount}")
