import logging

def market_order(client, symbol, side, quantity):

    order = client.create_order({
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity
    })

    logging.info(order)
    return order


def limit_order(client, symbol, side, quantity, price):

    order = client.create_order({
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC"
    })

    logging.info(order)
    return order
