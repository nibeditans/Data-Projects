class bike_shop:
    def __init__(self, stock):
        self.stock = stock

    def display_no_of_bikes(self):
        print("Total bikes available in stock currently: ", self.stock)

    def rent_for_bikes(self, quantity):
        if quantity <= 0:
            print("Please enter a positive value.")
        elif quantity > self.stock:
            print("Sorry! Currently, we have only 100 bikes in our stock.")
        else:
            self.stock -= quantity
            print("You need to pay for", quantity, "bikes in total: ", quantity * 100)
            print("\nUpdated just now! Total bikes available in stock now: ", self.stock - quantity)


while True:
    try:
        obj = bike_shop(1000)
        user_inp = int(input("""
    1. Display stock
    2. Rent a bike
    3. Exit
                            """))

        if user_inp == 1:
            obj.display_no_of_bikes()
        elif user_inp == 2:
            bike_qty = int(input("Please enter the number of bikes you want to rent: "))
            obj.rent_for_bikes(bike_qty)
        elif user_inp == 3:
                break
        else:
            print("What do you want dude? 😑 Please enter valid inputs.")
    except:
        print("Is it a number? Seriously dude, what's this now! 😐")

        user_choice = input("\nDo you want to continue? "
                            "\nType 'yes' if you're sure that you'll enter valid inputs! 😣"
                            "\nAnd if no, then type anything to exit. 🙄\n")
        if user_choice.lower() == 'yes':
            continue
        else:
            print("Exited. ")
            break
