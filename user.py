import sys
from function import *
from mainxyz import *

def user_page():
    print("========== Welcome to User-Page ==========")
    print("Enter 1 to Sign-up (If you are new)")
    print("Enter 2 to Login")
    print("Enter 3 to exit")
    print("Enter 4 to back to Main Menu")
    sys.exit()

    val = input("Enter the Value:-")

    if not val.isdigit():
        print("Error: Enter valid input")
    val = int(val)
    
    if val == 1:
        userSignup()
    elif val == 2:
        userLogin()
    elif val == 3:
        sys.exit()
    elif val == 4:
        exit()
    else:
        print("Enter: Enter valid input")
        user_page()


def userSignup():
    print("Welcome to Sign-up page")
    data = load_data("user.json")
    userId = input("Enter the id:-")
    if checkuserid(userId,"user.json"):
        print("Error: User id is already taken")
        userSignup()
    password = input("Enter the paddword:-")

    newAcc = {
        "id":userId,
        "password":password
    }

    data.append(newAcc)
    save_data(data)
    print("Your account has been signed-up")
    userMenu()

def userLogin():
    print("Welcome to user login page")
    data = load_data("user.json")
    userId = input("Enter the user-id:-")
    if not checkuserid(userId,"user.json"):
        print("Error: Enter the valid user-id")
        userLogin()
    password = input("Enter the password:-")

    for acc in data:
        if acc["id"] == userId and acc["password"] == password:
            userMenu()

def userMenu():
    print("Welcome to user Menu")
    print("Enter 1 to view Whole Inventory")
    print("Enter 2 to search product")
    print("Enter 3 to check product availability")
    print("Enter 4 to logout")

    val = input("Enter the value:-")

    if not val.isdigit():
        print("Error: Enter valid ")
    val = int(val)

    if val == 1:
        viewInventoryUser()
    elif val == 2:
        searchProduct()
    elif val == 3:
        checkAvailability()
    elif val == 4:
        sys.exit()
    else:
        print("Error: Enter the valid input")
        userMenu()
