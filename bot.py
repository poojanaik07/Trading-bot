import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Setup logger
        self.logger = logging.getLogger("trading_bot")
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler("trading_bot.log")
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='STOP_MARKET',
                    stopPrice=stop_price,
                    closePosition=False,
                    quantity=quantity,
                    timeInForce='GTC'
                )
            else:
                raise ValueError("Unsupported order type")

            self.logger.info(f"Order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Binance error: {e.message}")
            print(f"Binance error: {e.message}")
        except Exception as e:
            self.logger.error(f"Error placing order: {str(e)}")
            print(f"Error placing order: {str(e)}")
