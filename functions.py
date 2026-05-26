import os
import json

def view_files():
    with open("passwords.txt", "r") as f:
        contents = json.load(f)
        return contents

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

def view_password_for_website():
    password_for_website = input("Which website password you want: ")
    for item in view_files():

        if item["Website"] == password_for_website:
            print(f"Your password for the website {password_for_website} is {item["Password"]}")

def view_all_passwords():
    for item in view_files():
        for key, value in item.items():
            print(key, ":", value)
        print()

