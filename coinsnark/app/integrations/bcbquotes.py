import json
import logging
from urllib.parse import urlencode
from app.utils.requests import fetch_data
from app.utils.cache_data import save_data_to_cache


class BCBQuotes:
    @staticmethod
    def get_bcb_rates_data(cache):
        api_url = "https://www.bcb.gov.br/api/servico/sitebcb/indicadorCambio"
        
        # Obter os dados brutos da API
        data = fetch_data(api_url)
        
        # Decodificar os dados brutos e extrair informações relevantes
        bcb_rates_data = json.loads(data)
        currency_rates = {}

        # Iterar sobre os dados para extrair as cotações de USD e EUR em relação ao BRL
        for item in bcb_rates_data["conteudo"]:
            currency_name = item["moeda"]
            currency_buy_value = item["valorCompra"]

            # Salvar as cotações no dicionário
            currency_rates[currency_name] = currency_buy_value

        # Calcular o valor do BRL em relação ao USD (considerando USD como 1)
        brl_to_usd = currency_rates["Dólar"]
        
        # Calcular o valor do EUR em relação ao USD
        eur_to_brl = currency_rates["Euro"]
        #eur_to_usd = eur_to_brl / brl_to_usd
        eur_to_usd = round(eur_to_brl / brl_to_usd, 4)

        # Salvar os dados relevantes no cache
        exchange_rates = {"USD": 1, "BRL": brl_to_usd, "EUR": eur_to_usd}
        save_data_to_cache(exchange_rates, cache)

        logging.info("BCB Quotes cached")
        logging.info("Valor do BRL em relação ao USD: %.4f" % brl_to_usd)
        logging.info("Valor do EUR em relação ao USD: %.4f" % eur_to_usd)
        
        return exchange_rates
