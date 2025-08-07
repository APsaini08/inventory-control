import sys 
from function import *
from data import *

def admin_page():
    while True:
        print("========== Welcome to Admin-page ==========")
        print("Enter 1 to Sign-up (new-User)")
        print("Enter 2 to login")
        print("Enter 3 to exit")
        print("Enter 4 to go to Main-Menu")

        val = input("Enter the valur:-")

        if not val.isdigit():
            print("Error:Enter the valid input")
            admin_page()
        
        val = int(val)

        if val == 1:
            adminSignup()
        elif val == 2:
            adminLogin()
        elif val == 3:
            print("Thanks Good-Bye")
            sys.exit()
        elif val == 4:
            exit()

def adminSignup():
    print("Welcome to Admin Sign-up page")
    data = load_data("admin.json")
    adminId = input("Enter the id:-")
    
    if checkuserid(adminId,"admin.json"):
        print("Error: Entered Id is already Taken")
        adminSignup()
    password = input("Enter password:-")

    newAcc = {
        "id":adminId,
        "password":password
    }
    data.append(newAcc)
    save_data("user.json",data)
    print("Your account has been created Succesfully")
    adminMenu()

def adminLogin():
    while True:
        print("Welcome to Admin Login-page")
        data = load_data("admin.json")
        while True:
            adminId = input("Enter the id:-")
            if not checkuserid(adminId,"admin.json"):
                print("Error: Enter Valid Admin-Id")
                adminLogin()
            password = input("Enter password:-")

            for acc in data:
                if acc["id"] == id:
                    if acc["password"] == password :
                        adminMenu()
                    else:
                        print("Error: Enter correct password")
                        adminLogin()

def adminMenu():
    while True:
        print("Welcome to Admin Main-Menu")
        print("Enter 1 to Add Product")
        print("Enter 2 to Update-Product Quentity")
        print("Enter 3 to delete product")
        print("Enter 4 to View Whole Inventory")
        print("Enter 5 to Generate Report")
        print("Enter 6 to logout")

        val = input("Enter value:-")

        if not val.isdigit():
            print("Error: Enter valid input")
        val = int(val)

        if val == 1 :
            addproduct()
        elif val == 2 :
            updateProductQuentity()
        elif val == 3:
            deleteProduct()
        elif val == 4:
            viewInventoryAdmin()
        elif val == 5:
            generateReport()
        elif val == 6:
            sys.exit()