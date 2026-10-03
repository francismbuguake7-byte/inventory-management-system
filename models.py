"""In-memory inventory "database" and simple CRUD helper functions.

The inventory is just a normal Python list of dictionaries. Each item
looks like:

    {"id": 1, "product_name": "Milk", "quantity": 10, "price": 120.50}
"""

# This list acts as our in-memory database.
inventory = [
    {"id": 1, "product_name": "Milk", "quantity": 10, "price": 120.50},
    {"id": 2, "product_name": "Bread", "quantity": 5, "price": 45.00},
]


def get_all_items():
    """Return the whole inventory list."""
    return inventory


def get_item(item_id):
    """Return one item by id, or None if it is not found."""
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None


def next_id():
    """Work out the next id to use for a new item."""
    biggest = 0
    for item in inventory:
        if item["id"] > biggest:
            biggest = item["id"]
    return biggest + 1


def add_item(product_name, quantity, price):
    """Create a new item, add it to the list and return it."""
    item = {
        "id": next_id(),
        "product_name": product_name,
        "quantity": quantity,
        "price": price,
    }
    inventory.append(item)
    return item


def update_item(item_id, data):
    """Update an existing item with the given fields. Return it or None."""
    item = get_item(item_id)
    if item is None:
        return None
    if "product_name" in data:
        item["product_name"] = data["product_name"]
    if "quantity" in data:
        item["quantity"] = data["quantity"]
    if "price" in data:
        item["price"] = data["price"]
    return item


def delete_item(item_id):
    """Delete an item by id. Return True if deleted, else False."""
    item = get_item(item_id)
    if item is None:
        return False
    inventory.remove(item)
    return True


def reset_inventory():
    """Reset the inventory to its starting state (used by tests)."""
    inventory.clear()
    inventory.append({"id": 1, "product_name": "Milk", "quantity": 10, "price": 120.50})
    inventory.append({"id": 2, "product_name": "Bread", "quantity": 5, "price": 45.00})
