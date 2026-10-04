import requests
BARCODE_URL = 'https://world.openfoodfacts.org/api/v2/product/{code}.json'
SEARCH_URL = 'https://world.openfoodfacts.org/cgi/search.pl'

def to_local_format(name):
    return {'product_name': name, 'quantity': 1, 'price': 0}

def lookup_by_barcode(barcode):
    url = BARCODE_URL.format(code=barcode)
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data.get('status') == 1 and data.get('product'):
        name = data['product'].get('product_name', '')
        if name:
            return to_local_format(name)
    return None

def lookup_by_name(name):
    params = {'search_terms': name, 'search_simple': 1, 'action': 'process', 'json': 1, 'page_size': 1}
    response = requests.get(SEARCH_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    products = data.get('products', [])
    if len(products) > 0:
        found_name = products[0].get('product_name', '')
        if found_name:
            return to_local_format(found_name)
    return None
