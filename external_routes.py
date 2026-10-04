from flask import Blueprint, jsonify, request
import requests
import external_api
import models
helper = Blueprint('helper', __name__)

@helper.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Inventory Management API is running'})

def _lookup(barcode, name):
    if barcode:
        return external_api.lookup_by_barcode(barcode)
    return external_api.lookup_by_name(name)

@helper.route('/inventory/lookup', methods=['GET'])
def lookup():
    barcode = request.args.get('barcode')
    name = request.args.get('name')
    if not barcode and (not name):
        return (jsonify({'error': 'Please provide a barcode or name'}), 400)
    try:
        product = _lookup(barcode, name)
    except requests.RequestException:
        return (jsonify({'error': 'External API failure'}), 502)
    if product is None:
        return (jsonify({'error': 'Product not found'}), 404)
    return jsonify(product)

@helper.route('/inventory/import', methods=['POST'])
def import_product():
    data = request.get_json(silent=True) or {}
    barcode = data.get('barcode')
    name = data.get('name')
    if not barcode and (not name):
        return (jsonify({'error': 'Please provide a barcode or name'}), 400)
    try:
        product = _lookup(barcode, name)
    except requests.RequestException:
        return (jsonify({'error': 'External API failure'}), 502)
    if product is None:
        return (jsonify({'error': 'Product not found'}), 404)
    item = models.add_item(product['product_name'], product['quantity'], product['price'])
    return (jsonify(item), 201)
