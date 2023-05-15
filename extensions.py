import requests
import json
from config import keys

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: float):
        if quote == base:
            raise APIException(f"Unable to transfer identical currencies {base}.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Unable to process currency, Enter the name of the currency in the following format:\n \
                               rub/$/£/euro")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Unable to process currency {amount}.")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Unable to process amount {amount}.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]
        value = (total_base * amount)
        # text = f"Ценa {amount} {quote} - {value:.2f} {base}"

        return value







