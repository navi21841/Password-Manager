import os
import json

def add_password():
    while(True):

        confirmation = input("You want to Enter a New Password Enter (y/n): ").lower()

        if confirmation == "y":

            password = input("Enter the Password you want to add: ")
            website = input("Enter the name of the website: ")

            data = {
                "Website": website,
                "Password": password
            }

            if os.path.exists("passwords.txt"):

                with open("passwords.txt", "r") as f:
                    contents = json.load(f)

                contents.append(data)

                with open("passwords.txt", "w") as f:
                    json.dump(contents, f, indent=4)

            else:

                with open("passwords.txt", "w") as f:
                    json.dump([data], f, indent=4)
        elif(confirmation == "n"):
            print("No password was added")
            break
        else:
            print("Please enter y or n only")

add_password()
