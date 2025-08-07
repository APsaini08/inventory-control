import json
import os
from user import *
from admin import *

def mainxy():
    while True: 
        print("====== Welcome to Inventory Control System ======")
        print("Enter 1 to go to Admin-page")
        print("Enter 2 to go to User-page")
        print("Enter 3 to Exit")

        val = input("Enter your choice: ").strip()

        if not val.isdigit():
            print("Error: Please enter a number (1-3)\n")
            continue
        
        val = int(val)

        if val == 1:
            admin_page()
        elif val == 2:
            user_page()
        elif val == 3:
            print("Thank you for using Inventory Control System. Goodbye!")
            break  
        else:
            print("Error: Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    mainxy()
