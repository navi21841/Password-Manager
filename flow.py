import functions 
from functions import *

def flow():
    print("=" * 50)
    print("               PASSWORD MANAGER")
    print("=" * 50)

    while True:

        print("\n Press 1 to add password")
        print(" Press 2 to view password for a specific website")
        print(" Press 3 to view all the passwords you have saved")
        print(" Press 4 to Exit")

        answer = input("\n")
        if answer == "1":
            add_password()

        elif answer == "2":
            view_password_for_website()

        elif answer == "3":
            view_all_passwords()

        elif answer == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid Input")

flow()

