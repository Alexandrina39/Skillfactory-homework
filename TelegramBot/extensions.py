import requests
import json
from config import keys

class ConversionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException("It's impossible to convert the same currency")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f"Failed to process currency {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f"Failed to process currency {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Failed to process the amount {amount}")

        url = f'https://v6.exchangerate-api.com/v6/81f4dcc5adb8724817f258fb/latest/{quote_ticker}'
        response = requests.get(url)
        data = json.loads(response.text)

        converted_amount = amount * data['conversion_rates'][base_ticker]
        return converted_amount
