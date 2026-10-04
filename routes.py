
from flask import Blueprint, jsonify, request

import models
import validation

crud = Blueprint("crud", __name__)


@crud.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(models.get_all_items())


@crud.route("/inventory/<int:item_id>", methods=["GET"])
def get_one(item_id):
    item = models.get_item(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


@crud.route("/inventory", methods=["POST"])
def create():
    data = request.get_json(silent=True)
    error = validation.validate_new_item(data)
    if error is not None:
        return jsonify({"error": error}), 400
    item = models.add_item(data["product_name"], data["quantity"], data["price"])
    return jsonify(item), 201


@crud.route("/inventory/<int:item_id>", methods=["PATCH"])
def update(item_id):
    data = request.get_json(silent=True)
    error = validation.validate_update(data)
    if error is not None:
        return jsonify({"error": error}), 400
    item = models.update_item(item_id, data)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


@crud.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete(item_id):
    deleted = models.delete_item(item_id)
    if not deleted:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": "Item deleted"})
