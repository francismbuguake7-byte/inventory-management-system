def test_missing_name(client):
    response = client.post('/inventory', json={'quantity': 1, 'price': 1})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'product_name is required'

def test_missing_quantity(client):
    response = client.post('/inventory', json={'product_name': 'X', 'price': 1})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'quantity is required'

def test_missing_price(client):
    response = client.post('/inventory', json={'product_name': 'X', 'quantity': 1})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'price is required'

def test_invalid_quantity(client):
    data = {'product_name': 'X', 'quantity': 'ten', 'price': 1}
    response = client.post('/inventory', json=data)
    assert response.status_code == 400
    assert response.get_json()['error'] == 'quantity must be a number'

def test_invalid_price(client):
    data = {'product_name': 'X', 'quantity': 1, 'price': 'free'}
    response = client.post('/inventory', json=data)
    assert response.status_code == 400
    assert response.get_json()['error'] == 'price must be a number'

def test_negative_quantity(client):
    data = {'product_name': 'X', 'quantity': -5, 'price': 1}
    response = client.post('/inventory', json=data)
    assert response.status_code == 400
    assert response.get_json()['error'] == 'quantity cannot be negative'

def test_negative_price(client):
    data = {'product_name': 'X', 'quantity': 1, 'price': -2}
    response = client.post('/inventory', json=data)
    assert response.status_code == 400
    assert response.get_json()['error'] == 'price cannot be negative'

def test_missing_body(client):
    response = client.post('/inventory', data='', content_type='application/json')
    assert response.status_code == 400
