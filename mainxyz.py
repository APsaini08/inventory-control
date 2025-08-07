import json
import os
from user import *
from admin import *

def mainxy():
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
    else:
        print("Error: Enter the valid input")
        main()

def load_data(file):
    if not os.path.exists(file):
        with open(file , "w") as f1:
            json.dump([],f1)
    with open(file,"r") as f2:
        return json.load(f2)

def save_data(file,data):
    with open(file ,"w") as f:
        json.dump(data,f,indent=4)

def checkuserid(id,file):
    data = load_data(file)
    for account in data:
        if account["id"] == id:
            return True
    return False

if __name__ == "__main__":
    mainxy()