def bigger_price(limit, data):
    """
        TOP most expensive goods
    """
    # your code here
    return sorted(data, key=lambda k: k['price'], reverse=True)[:limit]

bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ])# == [ {"name": "wine", "price": 138},{"name": "bread", "price": 100}], "First"

bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ])# == [{"name": "whiteboard", "price": 170}], "Second"