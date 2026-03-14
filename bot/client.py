from binance.client import Client

TESTNET_URL = "https://testnet.binancefuture.com"

class BinanceClient:

    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = TESTNET_URL

    def create_order(self, params):
        return self.client.futures_create_order(**params)
