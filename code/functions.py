import os
import json

def view_files():
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as f:
            return json.load(f)
    else:
        return []

def add_password():
    while True:
        confirmation = input("You want to Enter a New Password Enter (y/n): ").lower()

        if confirmation == "y":
            password = input("Enter the Password you want to add: ")
            website = input("Enter the name of the website: ")

            data = {
                "Website": website,
                "Password": password
            }

            contents = view_files()
            contents.append(data)

            with open("passwords.txt", "w") as f:
                json.dump(contents, f, indent=4)

            print("Password added")

        elif confirmation == "n":
            print("No password was added")
            break

        else:
            print("Please enter y or n only")

def view_password_for_website():
    password_for_website = input("Which website password you want: ")
    try:
        for item in view_files():
            if item["Website"] == password_for_website:
                print(f"Your password for the website {password_for_website} is {item['Password']}")
                return
    except:
        print("Error")   

def view_all_passwords():
    try:
        for item in view_files():
            for key, value in item.items():
                print(key, ":", value)
            print()
    except:
        print("Error")
def remove_password():
    while True:
        confirmation = input("Do you want to remove the password (y/n): ").lower()

        if confirmation == "y":
            print("These are all the websites saved you can choose any website to delete")
            view_all_passwords()

            website_to_delete = input("Enter the name of the website which you want to remove the password of: ")

            contents = view_files()

            found = False

            for item in contents:
                if item["Website"] == website_to_delete:
                    contents.remove(item)
                    found = True
                    break

            if found:
                with open("passwords.txt", "w") as f:
                    json.dump(contents, f, indent=4)
                print("Password deleted")
            else:
                print("The website you entered does not exist")

        elif confirmation == "n":
            print("No password was deleted")
            break

        else:
            print("Please enter y or n only")
