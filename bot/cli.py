import argparse
from bot.client import BinanceClient
from bot.orders import market_order, limit_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

validate_inputs(args.side, args.type, args.price)

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET"

client = BinanceClient(API_KEY, API_SECRET)

if args.type == "MARKET":

    order = market_order(
        client,
        args.symbol,
        args.side,
        args.quantity
    )

else:

    order = limit_order(
        client,
        args.symbol,
        args.side,
        args.quantity,
        args.price
    )

print(order)
