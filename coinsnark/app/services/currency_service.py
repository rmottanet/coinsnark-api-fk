from coinsnark.app.utils import get_cache_contents, get_currency_name
from coinsnark.app.models import CurrencyResponse, ErrorResponse

def get_all_currency_names(cache):
    """
    Retorna um dicionário com todas as siglas de moeda no cache e seus respectivos nomes humanos.

    Args:
    - cache: O objeto de cache onde os dados estão armazenados.

    Returns:
    Um objeto CurrencyResponse contendo as siglas de moeda como chaves e os nomes humanos correspondentes como valores,
    ou um objeto ErrorResponse em caso de falha.
    """
    try:
        cached_contents = get_cache_contents(cache)
        if cached_contents is None:
            raise ValueError("Cache is empty or inaccessible.")

        all_currency_names = {}
        currency_codes = [key for key in cached_contents.keys()]
        
        for currency_code in currency_codes:
            currency_name = get_currency_name(currency_code)
            if currency_name:
                all_currency_names[currency_code] = currency_name
            else:
                # Considerando a possibilidade de não conseguir obter o nome de alguma moeda específica
                all_currency_names[currency_code] = "Unknown"

        return CurrencyResponse(all_currency_names)
    except Exception as e:
        return ErrorResponse(str(e))
