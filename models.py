inventory = [{'id': 1, 'product_name': 'Milk', 'quantity': 10, 'price': 120.5}, {'id': 2, 'product_name': 'Bread', 'quantity': 5, 'price': 45.0}]

def get_all_items():
    return inventory

def get_item(item_id):
    for item in inventory:
        if item['id'] == item_id:
            return item
    return None

def next_id():
    biggest = 0
    for item in inventory:
        if item['id'] > biggest:
            biggest = item['id']
    return biggest + 1

def add_item(product_name, quantity, price):
    item = {'id': next_id(), 'product_name': product_name, 'quantity': quantity, 'price': price}
    inventory.append(item)
    return item

def update_item(item_id, data):
    item = get_item(item_id)
    if item is None:
        return None
    if 'product_name' in data:
        item['product_name'] = data['product_name']
    if 'quantity' in data:
        item['quantity'] = data['quantity']
    if 'price' in data:
        item['price'] = data['price']
    return item

def delete_item(item_id):
    item = get_item(item_id)
    if item is None:
        return False
    inventory.remove(item)
    return True

def reset_inventory():
    inventory.clear()
    inventory.append({'id': 1, 'product_name': 'Milk', 'quantity': 10, 'price': 120.5})
    inventory.append({'id': 2, 'product_name': 'Bread', 'quantity': 5, 'price': 45.0})
