import sys
from function import *
from data import *

def user_page():
    while True:
        print("========== Welcome to User Page ==========")
        print("1. Sign-up (New User)")
        print("2. Login")
        print("3. Exit")

        val = input("Enter your choice: ").strip()

        if not val.isdigit():
            print("Error: Please enter a valid number (1-3)\n")
            continue

        val = int(val)

        if val == 1:
            userSignup()
        elif val == 2:
            userLogin()
        elif val == 3:
            print("Thank you! Exiting User Page.")
            break
        else:
            print("Error: Please enter a correct input (1-3)\n")

def userSignup():
    print("\n===== User Sign-up Page =====")
    data = load_data("user.json")
    userId = input("Enter new User ID: ").strip()

    if checkuserid(userId, "user.json"):
        print("Error: This User ID is already taken.\n")
        return

    password = input("Enter password: ").strip()

    newAcc = {
        "id": userId,
        "password": password
    }

    data.append(newAcc)
    save_data("user.json", data)
    print("Your account has been successfully created!\n")

def userLogin():
    print("\n===== User Login Page =====")
    data = load_data("user.json")

    while True:
        userId = input("Enter User ID (or type 'exit' to cancel): ").strip()
        if userId.lower() == "exit":
            return

        if not checkuserid(userId, "user.json"):
            print("Error: User ID does not exist.\n")
            continue

        password = input("Enter password: ").strip()

        for acc in data:
            if acc["id"] == userId:
                if acc["password"] == password:
                    print("Login successful!\n")
                    userMenu()
                    return
                else:
                    print("Error: Incorrect password.\n")
                    break 

def userMenu():
    while True:
        print("===== User Menu =====")
        print("1. View Entire Inventory")
        print("2. Search Product")
        print("3. Check Product Availability")
        print("4. Logout")

        val = input("Enter your choice: ").strip()

        if not val.isdigit():
            print("Error: Please enter a valid number.\n")
            continue

        val = int(val)

        if val == 1:
            viewInventoryUser()
        elif val == 2:
            searchProduct()
        elif val == 3:
            checkAvailability()
        elif val == 4:
            print("Logging out...\n")
            return
        else:
            print("Invalid option. Try again.\n")
