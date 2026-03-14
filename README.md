# Binance Futures Testnet Trading Bot

This is a simple Python CLI trading bot that places orders on Binance Futures Testnet.

## Setup

pip install -r requirements.txt

## Example

Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
