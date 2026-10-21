vending = {
    "1": ("Chips", 100),
    "2": ("Chocolate", 120),
    "3": ("Soda", 150),
    "4": ("Water", 50)
} 
# set with items and prices

print("Menu:")
for option, (item, price) in vending.items():
    print(f"{option}. {item} - {price}p")
# assigns item and price to objects in the vending set, then prints in menu format

print("5. Quit")
choice = input("What would you like to buy? ")
# prints a quit option, as i found this hard to do within the set, then asks for user input

if choice == "5":
    print("Thank you for using the vending machine!")
elif choice in vending:
    item, price = vending[choice]
    print(f"You have selected {item}. This item is {price}p.")
else:
    print("Invalid selection.")
# checks if user input is valid, if not prints invalid selection, if yes prints item and price, if 5 prints thank you message

balance = int(input("Please enter the amount of money you have (in pence): ")) # it said 200, but i prefer more input

if choice in vending:
    if balance >= price:
        balance -= price
        print("Purchase successful.")
        print(f"Your remaining balance is {balance}p.")
    else:
        print("Insufficient funds. Please choose a cheaper product, or quit.")

run = choice != "5"

while run:
    print("Menu:")
    for option, (item, price) in vending.items():
        print(f"{option}. {item} - {price}p")

    print("5. Quit")
    choice = input("What would you like to buy? ")

    if choice == "5":
        print("Thank you for using the vending machine!")
        run = False
    elif choice in vending:
        item, price = vending[choice]
        print(f"You have selected {item}. This item is {price}p.")

        if balance >= price:
            balance -= price
            print("Purchase successful.")
            print(f"Your remaining balance is {balance}p.")
        else:
            print("Insufficient funds. Please choose a cheaper product, or quit.")
    else:
        print("Invalid selection.")

