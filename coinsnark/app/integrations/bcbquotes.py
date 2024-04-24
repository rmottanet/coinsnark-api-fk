import json
import logging
from urllib.parse import urlencode
from coinsnark.app.utils.requests import fetch_data
from coinsnark.app.utils.cache_data import save_data_to_cache

class BCBQuotes:
    @staticmethod
    def get_bcb_rates_data(cache):
        api_url = "https://www.bcb.gov.br/api/servico/sitebcb/indicadorCambio"
        
        data = fetch_data(api_url)
        
        bcb_rates_data = json.loads(data)
        currency_rates = {}

        for item in bcb_rates_data["conteudo"]:
            currency_name = item["moeda"]
            currency_buy_value = float(item["valorCompra"])

            currency_rates[currency_name] = currency_buy_value

        usd_to_brl = currency_rates["Dólar"]
        
        brl_to_eur = 1 / currency_rates["Euro"]
        usd_to_eur = usd_to_brl * brl_to_eur

        # cache data
        exchange_rates = {"USD": 1, "BRL": usd_to_brl, "EUR": round(usd_to_eur, 4)}
        save_data_to_cache(exchange_rates, cache)

        logging.info("BCB Quotes cached")
        logging.info("Exchange Rates: USD to BRL = {:.4f}, USD to EUR = {:.4f}".format(usd_to_brl, usd_to_eur))
        
        return exchange_rates

