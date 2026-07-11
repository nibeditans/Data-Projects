class bike_shop:
    def __init__(self, stock):
        self.stock = stock
    def display_no_of_bikes(self):
        print("Total bikes available now: ", self.stock)
    def rent_for_bikes(self, qantity):
        if qantity <= 0:
            print("Please enter a positive value. ")
        elif qantity > self.stock:
            print("Sorry! Currently, we have only 100 bikes in our stock.")
        else:
            print("Total Price: ", qantity * 100)
            print("Updated just now! Total bikes available now: ", self.stock - qantity)

while True:
    obj = bike_shop(100)
    user_inp = int(input("""
1. Display stock
2. Rent a bike
3. Exit
                         """))
    if user_inp == 1:
        obj.display_no_of_bikes()
    elif user_inp == 2:
        bike_qty = int(input("Please, enter the amount of bikes you want for rent: "))
        obj.rent_for_bikes(bike_qty)
    elif user_inp == 3:
        print("Exited a moment ago.  ")
        break
    else:
        print("What do you want dude? Please enter valid inputs.")
