import requests
import external_api
import models

def view_inventory():
    for item in models.get_all_items():
        print(item)

def add_item():
    name = input('Product name: ')
    quantity = int(input('Quantity: '))
    price = float(input('Price: '))
    item = models.add_item(name, quantity, price)
    print('Added:', item)

def update_item():
    item_id = int(input('Item id to update: '))
    quantity = int(input('New quantity: '))
    price = float(input('New price: '))
    item = models.update_item(item_id, {'quantity': quantity, 'price': price})
    if item is None:
        print('Item not found')
    else:
        print('Updated:', item)

def delete_item():
    item_id = int(input('Item id to delete: '))
    if models.delete_item(item_id):
        print('Item deleted')
    else:
        print('Item not found')

def search_api():
    name = input('Product name to search: ')
    try:
        product = external_api.lookup_by_name(name)
    except requests.RequestException:
        print('External API failure')
        return
    if product is None:
        print('Product not found')
    else:
        print('Found:', product)

def import_api():
    name = input('Product name to import: ')
    try:
        product = external_api.lookup_by_name(name)
    except requests.RequestException:
        print('External API failure')
        return
    if product is None:
        print('Product not found')
        return
    item = models.add_item(product['product_name'], product['quantity'], product['price'])
    print('Imported:', item)
