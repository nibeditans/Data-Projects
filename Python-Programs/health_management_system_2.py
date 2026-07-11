# Define the three persons
persons = ["NS", "Nate", "Nibedita"]

# Define the two options
options = ["log", "retrieve"]

# Define the two categories
categories = ["exercise", "food"]


# Define a function to log or retrieve data
def health_management_system():
    # Get the person's name
    person = input("Enter person's name (NS, Nate, or Nibedita): ")
    if person not in persons:
        print("Invalid person's name!")
        return

    # Get the user's option
    option = input("Enter option (log or retrieve): ")
    if option not in options:
        print("Invalid option!")
        return

    # Get the category
    category = input("Enter category (exercise or food): ")
    if category not in categories:
        print("Invalid category!")
        return

    # Define the filename
    filename = person + "_" + category + ".txt"

    if option == "log":
        # Get the data to log
        data = input("Enter data to log: ")

        # Write the data to the file
        with open(filename, "a") as f:
            f.write(data + "\n")

        print("Data logged successfully!")
    else:
        # Read the data from the file
        with open(filename, "r") as f:
            data = f.read()

        # Print the data
        print(data)


# Call the function to start the program
health_management_system()
