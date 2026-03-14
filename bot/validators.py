def validate_inputs(side, order_type, price):

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order needs a price")
