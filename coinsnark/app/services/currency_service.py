from app.utils.currency_data import get_currency_name
from app.utils.cache_data import get_cache_contents


def get_all_currency_names(cache):
    """
    Retorna um dicionário com todas as siglas de moeda no cache e seus respectivos nomes humanos.

    Args:
    - cache: O objeto de cache onde os dados estão armazenados.

    Returns:
    Um dicionário contendo as siglas de moeda como chaves e os nomes humanos correspondentes como valores.
    """
    all_currency_names = {}
    cached_contents = get_cache_contents(cache)

    if cached_contents:
        currency_codes = [key for key in cached_contents.keys()]
        
        for currency_code in currency_codes:
            currency_name = get_currency_name(currency_code)
            all_currency_names[currency_code] = currency_name

    return all_currency_names
