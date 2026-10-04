
def is_number(value):
    if isinstance(value, bool):
        return False
    return isinstance(value, int) or isinstance(value, float)


def validate_new_item(data):
    if data is None:
        return "Missing JSON body"

    if "product_name" not in data or data["product_name"] == "":
        return "product_name is required"

    if "quantity" not in data:
        return "quantity is required"
    if not is_number(data["quantity"]):
        return "quantity must be a number"
    if data["quantity"] < 0:
        return "quantity cannot be negative"

    if "price" not in data:
        return "price is required"
    if not is_number(data["price"]):
        return "price must be a number"
    if data["price"] < 0:
        return "price cannot be negative"

    return None


def validate_update(data):
    if data is None:
        return "Missing JSON body"
    if len(data) == 0:
        return "Empty update request"

    if "quantity" in data:
        if not is_number(data["quantity"]):
            return "quantity must be a number"
        if data["quantity"] < 0:
            return "quantity cannot be negative"

    if "price" in data:
        if not is_number(data["price"]):
            return "price must be a number"
        if data["price"] < 0:
            return "price cannot be negative"

    return None
