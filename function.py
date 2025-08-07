import os
import json
from data import *

def addproduct():
    print("Welcome To Inventory Control (Here you can add product)")
    while True:
        pId = input("Enter the product ID:-")
        pName = input("Enter the product name/(exit go to main Menu):-")
        pType = input("Enter the product type:-")
        pQuentity = int(input("Enter the Quentity of product:-"))
        pSoled = input("Quentity solled:-")

        data = load_data("store.json")
        if pName.lower() == "exit":
            break
        product = {
            "P-ID":pId,
            "Name":pName,
            "Type":pType,
            "Quentity":pQuentity,
            "Solled":pSoled,
            "Status":"Available"
        }
        data.append(product)
    save_data(data)
    adminMenu()

def checkProductId(Id):
    data = load_data("store.json")
    for product in data:
        if product["P-ID"] == Id:
            return True
    
    return False

def updateProductQuentity():
    print("Welcome to inventory control Here you can update the Quentity of Product")
    data = load_data("store.json")
    while True:
        pId = input("Enter the Product Id/exit to admin Menu:-")
        if pId.lower() == "exit":
            adminMenu()
        if not checkProductId(pId):
            print("Error: Enter the correct Product-ID")
            updateProductQuentity()
            break
        pQuentity = int(input("Enter the Quentity to ADD:-"))
        for product in data :
            if product["P_ID"] == pId:
                product["Quentity"] += pQuentity
                save_data(data)
                break
    adminMenu()

def deleteProduct():
    print("Welcome to Inventory Control Here you can Delete the product")
    data = load_data("store.json")
    while True:
        pId = input("Enter the Product id/exit to go to admin menu:-")

        if pId.lower == "exit":
            adminMenu()
        if not checkProductId(pId):
            print("Erro: Enter valid Product Id")
            deleteProduct()
            break
        for product in data:
            if product["P-ID"] == pId:
                product["Status"] = "Deleted"
                break
        deleteProduct()

def viewInventoryAdmin():
    print("Welcome to Inventory Control System - Here is you all Inventory")
    data = load_data("store.json")
    print("P-ID    Product-Name    Product-Type    Product-Quentity    Product-Solled    Product-Status")
    for product in data:
        print(f"{product["P-ID"]}    {product["Name"]}    {product["Type"]}    {product["Quentity"]}    {product["Solled"]}    {product["Status"]}")

    adminMenu()

def generateReport():
    print("Wait for few second you will get the report in txt format")
    data = load_data("store.json")
    with open("report.txt", "w") as report:
        print("Product-Id       Product-Name        Product-Type        Product-Quentity        Product-Solled      Product-Status")
        for user in data:
            report.write(f"{product[P-ID]}      {product[Name]}       {product["Type"]}      {product["Quentity"]}      {product["Solled"]}     {product["Status"]}")
    adminMenu()


def viewInventoryUser():
    print("Welcome to Inventory Control System - Here is you all Inventory")
    data = load_data("store.json")
    print("P-ID    Product-Name    Product-Type")
    for product in data:
        if product["Status"] == "Not-Available":
            continue
        print(f"{product["P-ID"]}    {product["Name"]}    {product["Type"]}")
    
    userMenu()
def searchProduct():
    print("Welcome to Inventory-control System (Here you can search Product)")
    data = load_data("store.json")

    ptype = input("Enter product-ID")

    for product in data:
        if product["Type"] == ptype:
            print(product["Name"])
        
    userMenu()

def checkAvailability():
    print("Welcome to Inventory-Control (Here you can Check the Availability of product)")

    pId = input("Enter the product-Id:-")

    if not checkProductId(pId):
        print("Error: Enter Correct Product-Id")
        checkAvailability()
    for product in data:
        if product["Status"] == "Available":
            print("Product is Available")
            break

    userMenu()