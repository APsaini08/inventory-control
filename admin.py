import sys
from function import *
from data import *

def admin_page():
    while True:
        print("========== Welcome to Admin Page ==========")
        print("1. Sign-up (New User)")
        print("2. Login")
        print("3. Exit")
        print("4. Return to Main Menu")

        val = input("Enter your choice: ").strip()

        if not val.isdigit():
            print("Error: Please enter a valid number (1-4)\n")
            continue

        val = int(val)

        if val == 1:
            adminSignup()
        elif val == 2:
            if adminLogin():
                adminMenu()
        elif val == 3:
            print("Thanks. Goodbye!")
            sys.exit()
        elif val == 4:
            break  
        else:
            print("Invalid input. Please select a valid option.\n")

def adminSignup():
    print("\n===== Admin Sign-up Page =====")
    data = load_data("admin.json")
    adminId = input("Enter new Admin ID: ").strip()

    if checkuserid(adminId, "admin.json"):
        print("Error: ID already exists. Please try again.\n")
        return

    password = input("Enter password: ").strip()

    newAcc = {
        "id": adminId,
        "password": password
    }

    data.append(newAcc)
    save_data("admin.json", data)
    print("Your account has been created successfully!\n")

def adminLogin():
    print("\n===== Admin Login Page =====")
    data = load_data("admin.json")

    while True:
        adminId = input("Enter Admin ID (or type 'exit' to cancel): ").strip()
        if adminId.lower() == "exit":
            return

        if not checkuserid(adminId, "admin.json"):
            print("Error: Invalid Admin ID. Try again.\n")
            continue

        password = input("Enter password: ").strip()

        for acc in data:
            if acc["id"] == adminId:
                if acc["password"] == password:
                    print("Login successful!\n")
                    return True
                else:
                    print("Error: Incorrect password.\n")
                    break 
        return False

def adminMenu():
    while True:
        print("===== Admin Main Menu =====")
        print("1. Add Product")
        print("2. Update Product Quantity")
        print("3. Delete Product")
        print("4. View Entire Inventory")
        print("5. Generate Report")
        print("6. Logout")

        val = input("Enter your choice: ").strip()

        if not val.isdigit():
            print("Error: Please enter a valid number.\n")
            continue

        val = int(val)

        if val == 1:
            addproduct()
        elif val == 2:
            updateProductQuentity()
        elif val == 3:
            deleteProduct()
        elif val == 4:
            viewInventoryAdmin()
        elif val == 5:
            generateReport()
        elif val == 6:
            print("Logged out successfully.\n")
            return 
        else:
            print("Invalid option. Try again.\n")
