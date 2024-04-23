# coinsnark/coinsnark.app.integrations/exchangerates.py
import os
import json
import logging
from urllib.parse import urlencode
from coinsnark.app.utils import fetch_data, save_data_to_cache


class ExchangeRates:
    @staticmethod
    def get_exchange_rates_data(cache):
        api_key = os.getenv('EXCHANGE_RATES_API_KEY')
        if not api_key:
            raise RuntimeError("Chave 'EXCHANGE_RATES_API_KEY' não encontrada nas variáveis de ambiente")

        api_url = "https://exchange-rates.abstractapi.com/v1/live" 

        params = {
            "api_key": api_key,
            "base": "USD"  
        }

        full_url = f"{api_url}?{urlencode(params)}"

        try:

            data = fetch_data(full_url)

            exchange_rates_data = json.loads(data)

            base_currency = exchange_rates_data["base"]
            rates = exchange_rates_data["exchange_rates"] 

            for currency_code, rate in rates.items():
                # Formatar a chave para salvar no cache 
                cache_key = f"{currency_code}"
                cache_value = rate

                data_to_cache = {cache_key: cache_value}

                save_data_to_cache(data_to_cache, cache)

            logging.info("Exchange Rates successfully cached")

            return {"base": base_currency, "last_updated": exchange_rates_data.get("last_updated"), "rates": rates}

        except Exception as e:
            logging.error(f"Erro ao acessar a API de taxas de câmbio: {e}")
            raise
