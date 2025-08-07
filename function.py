import os
import json
from data import *

def addproduct():
    print("\n=== Add Product to Inventory ===")
    while True:
        pId = input("Enter Product ID/exit: ")
        if pId.strip().lower() == "exit":
            return
        if checkProductId(pId):
            print("Error: Product ID already exists.\n")
            continue

        pName = input("Enter Product Name (type 'exit' to return): ").strip()
        if pName.lower() == "exit":
            break

        pType = input("Enter Product Type: ")
        try:
            pQuantity = int(input("Enter Quantity: "))
            pSold = int(input("Enter Quantity Sold: "))
        except ValueError:
            print("Error: Quantity must be a number.")
            continue

        product = {
            "P-ID": pId,
            "Name": pName,
            "Type": pType,
            "Quantity": pQuantity,
            "Sold": pSold,
            "Status": "Available"
        }

        data = load_data("store.json")
        data.append(product)
        save_data("store.json", data)
        print("Product added successfully!\n")



def checkProductId(Id):
    data = load_data("store.json")
    for product in data:
        if product["P-ID"] == Id:
            return True
    return False


def updateProductQuentity():
    print("\n=== Update Product Quantity ===")
    data = load_data("store.json")
    while True:
        pId = input("Enter Product ID (or type 'exit' to return): ")
        if pId.lower() == "exit":
            break

        if not checkProductId(pId):
            print("Error: Product ID not found.\n")
            continue

        try:
            addQty = int(input("Enter Quantity to ADD: "))
        except ValueError:
            print("Error: Quantity must be a number.\n")
            continue

        for product in data:
            if product["P-ID"] == pId:
                product["Quantity"] += addQty
                save_data("store.json", data)
                print("Quantity updated successfully!\n")
                break



def deleteProduct():
    print("\n=== Delete Product ===")
    data = load_data("store.json")

    while True:
        pId = input("Enter Product ID to delete (or 'exit'): ").strip()
        if pId.lower() == "exit":
            break

        if not checkProductId(pId):
            print("Error: Invalid Product ID.\n")
            continue

        for product in data:
            if product["P-ID"] == pId:
                product["Status"] = "Deleted"
                save_data("store.json", data)
                print(f"Product {pId} marked as Deleted.\n")
                break



def viewInventoryAdmin():
    print("\n=== Full Inventory (Admin View) ===")
    data = load_data("store.json")
    print("P-ID\tName\t\tType\t\tQuantity\tSold\t\tStatus")
    for product in data:
        print(f'{product["P-ID"]}\t{product["Name"]}\t{product["Type"]}\t{product["Quantity"]}\t\t{product["Sold"]}\t\t{product["Status"]}')
 


def generateReport():
    print("Generating report...")
    data = load_data("store.json")

    with open("report.txt", "w") as report:
        report.write("P-ID\tName\tType\tQuantity\tSold\tStatus\n")
        for product in data:
            report.write(f'{product["P-ID"]}\t{product["Name"]}\t{product["Type"]}\t{product["Quantity"]}\t\t{product["Sold"]}\t{product["Status"]}\n')

    print("Report generated as 'report.txt'.")



def viewInventoryUser():
    print("\n=== Inventory (User View) ===")
    data = load_data("store.json")
    print("P-ID\tName\tType")
    for product in data:
        if product["Status"].lower() != "available":
            continue
        print(f'{product["P-ID"]}\t{product["Name"]}\t{product["Type"]}')



def searchProduct():
    print("\n=== Search Product by Type ===")
    data = load_data("store.json")
    pType = input("Enter Product Type: ").strip()

    found = False
    for product in data:
        if product["Type"].lower() == pType.lower() and product["Status"].lower() == "available":
            print(f'Found: {product["Name"]} (ID: {product["P-ID"]})')
            found = True

    if not found:
        print("No matching products found.")




def checkAvailability():
    print("\n=== Check Product Availability ===")
    data = load_data("store.json")
    pId = input("Enter Product ID: ").strip()

    if not checkProductId(pId):
        print("Error: Invalid Product ID.\n")
        return

    for product in data:
        if product["P-ID"] == pId:
            if product["Status"].lower() == "available":
                print("Product is Available.")
            else:
                print("Product is NOT Available.")
            break
