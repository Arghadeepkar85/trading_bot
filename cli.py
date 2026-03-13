import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

if args.type == "MARKET":
    result = place_market_order(args.symbol, args.side, args.quantity)
else:
    result = place_limit_order(args.symbol, args.side, args.quantity, args.price)

print("Order Result:")
print(result)
