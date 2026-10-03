"""The individual actions used by the CLI menu.

Each function uses simple input() and print() calls and talks to the
models and external_api modules directly (no duplicated logic).
"""
import requests

import external_api
import models


def view_inventory():
    """Print every item in the inventory."""
    for item in models.get_all_items():
        print(item)


def add_item():
    """Ask the user for details and add a new item."""
    name = input("Product name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    item = models.add_item(name, quantity, price)
    print("Added:", item)


def update_item():
    """Ask the user which item to update and change its fields."""
    item_id = int(input("Item id to update: "))
    quantity = int(input("New quantity: "))
    price = float(input("New price: "))
    item = models.update_item(item_id, {"quantity": quantity, "price": price})
    if item is None:
        print("Item not found")
    else:
        print("Updated:", item)


def delete_item():
    """Ask the user which item to delete and remove it."""
    item_id = int(input("Item id to delete: "))
    if models.delete_item(item_id):
        print("Item deleted")
    else:
        print("Item not found")


def search_api():
    """Search OpenFoodFacts by name and print the result."""
    name = input("Product name to search: ")
    try:
        product = external_api.lookup_by_name(name)
    except requests.RequestException:
        print("External API failure")
        return
    if product is None:
        print("Product not found")
    else:
        print("Found:", product)


def import_api():
    """Search OpenFoodFacts and add the found product to the inventory."""
    name = input("Product name to import: ")
    try:
        product = external_api.lookup_by_name(name)
    except requests.RequestException:
        print("External API failure")
        return
    if product is None:
        print("Product not found")
        return
    item = models.add_item(product["product_name"], product["quantity"], product["price"])
    print("Imported:", item)
