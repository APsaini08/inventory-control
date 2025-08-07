import json
import os
from user import *
from admin import *

def mainxy():
    while True: 
        print("======Welcome to Inventory Control System ======")
        print("Enter 1 to go to Admin-page")
        print("Enter 2 to go to User-page")
        print("Enter 3 to exit")
        val = input("Enter the value:-")

        if not val.isdigit():
            print("Error: Enter the valid input")
        val = int(val)

        if val == 1:
            admin_page()
        elif val == 2:
            user_page()
        elif val ==3:
            exit()


if __name__ == "__main__":
    mainxy()