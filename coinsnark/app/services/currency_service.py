# -*- coding: utf-8 -*-
from coinsnark.app.utils import get_cache_contents, get_currency_name
from coinsnark.app.models import CurrencyResponse, ErrorResponse

def get_all_currency_names(cache):
    """
    Returns a dictionary with all currency acronyms in the cache and their respective human names.

    Args:
    - cache: The cache object where the data is stored.

    Returns:
    A CurrencyResponse object containing the currency acronyms as keys and the corresponding human names as values,
    or an ErrorResponse object in case of failure.
    """
    try:
        cached_contents = get_cache_contents(cache)
        if cached_contents is None:
            raise ValueError("Cache is empty or inaccessible.")

        all_currency_names = {}
        
        # Filter currencies codes
        currency_codes = [key for key in cached_contents.keys() if len(key) == 3]
        
        for currency_code in currency_codes:
            currency_name = get_currency_name(currency_code)
            if currency_name:
                all_currency_names[currency_code] = currency_name
            else:
                # Considering the possibility of not being able to obtain the name of a specific currency
                all_currency_names[currency_code] = "Unknown"

        return CurrencyResponse(all_currency_names)
    except Exception as e:
        return ErrorResponse(str(e))
