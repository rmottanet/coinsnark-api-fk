# -*- coding: utf-8 -*-
import os
import json
import logging
from coinsnark.app.utils.requests import fetch_data
from coinsnark.app.utils.cache_data import save_data_to_cache
from datetime import datetime

class dRatesFK:
    @staticmethod
    def get_drates_fk_data(cache):
        api_key = os.getenv('COINSNARK_TOKEN')
        if not api_key:
            raise RuntimeError("Chave 'COINSNARK_TOKEN' não encontrada nas variáveis de ambiente")

        api_url = "https://drates-mssl-fk.vercel.app/exrates"

        headers = {'Authorization': f'Bearer {api_key}'}

        try:

            data = fetch_data(api_url, headers=headers)

            dRatesFK_data = json.loads(data)

            # Process data
            rates = dRatesFK_data

            for currency_code, rate in rates.items():
                # rates to float
                if len(currency_code) == 3:
                    rate = float(rate)

                cache_key = currency_code
                cache_value = rate

                if currency_code == "DATA_BASE":
                    utc_date = rate
                    formatted_date = datetime.strptime(utc_date, '%Y-%m-%d %H:%M:%S %Z')
                    cache_value = formatted_date

                # Save to cache
                save_data_to_cache({cache_key: cache_value}, cache)

            logging.info("dRates-FK successfully cached")

        except Exception as e:
            logging.error(f"Error accessing the API dRates-FK: {e}")
            raise
