from datetime import datetime
from app.utils import get_exchange_rate
from app.models import ConversionResponse, ErrorResponse

def convert_currency(cache, from_currency, to_currency, amount):
    """
    Converte uma determinada quantidade de uma moeda para outra.

    Args:
    - cache: O objeto de cache onde os dados estão armazenados.
    - from_currency: A sigla da moeda de origem.
    - to_currency: A sigla da moeda de destino.
    - amount: A quantidade da moeda de origem a ser convertida.

    Returns:
    Um objeto ConversionResponse contendo a quantidade convertida e o timestamp do cache.
    """
    try:
        # get exchange rate
        from_rate = get_exchange_rate(cache, from_currency)
        to_rate = get_exchange_rate(cache, to_currency)

        if from_rate is None or to_rate is None:
            raise Exception("Error getting exchange rates from cache")

        # calcule exchange rate e convert
        if from_rate != 0:
            exchange_rate = to_rate / from_rate
            converted_amount = amount * exchange_rate
            
            # try get cache time
            cache_updated = getattr(cache, 'updated_on', datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
            
            conversion_info = {
                "cache_updated": cache_updated,
                "from": from_currency,
                "to": to_currency,
                "converted": round(converted_amount, 2)
            }
            
            return ConversionResponse(conversion_info)
        else:
            raise Exception("Conversion rate cannot be zero")
    except Exception as e:
        return ErrorResponse(str(e))
