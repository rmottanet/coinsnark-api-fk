# coinsnark/app/utils/cache_data.py

DEFAULT_EXPIRATION_SECONDS = 3600 * 6  # 6 horas em segundos

def save_data_to_cache(data, cache):
    """
    Salva os dados no cache com um tempo de expiração padrão.
    
    Args:
    - data: Um dicionário contendo os dados a serem armazenados no cache.
    - cache: O objeto de cache onde os dados serão armazenados.
    """
    for key, value in data.items():
        cache.set(key, value, timeout=DEFAULT_EXPIRATION_SECONDS)


def get_cache_contents(cache):
    """
    Recupera e retorna todo o conteúdo do cache.

    Args:
    - cache: O objeto de cache a ser consultado.

    Returns:
    - Um dicionário contendo todas as chaves e seus valores correspondentes no cache.
    """
    cache_contents = {}
    
    for key in cache.cache._cache.keys():
        cache_contents[key] = cache.get(key)
	
    return cache_contents


def get_exchange_rate(cache, code):
    """
    Retorna a taxa de câmbio correspondente a um determinado código de moeda.

    Args:
    - cache: O objeto de cache onde as taxas de câmbio estão armazenadas.
    - code: O código da moeda para a qual desejamos obter a taxa de câmbio.

    Returns:
    - O valor da taxa de câmbio da moeda especificada, se existir. Caso contrário, retorna None.
    """
    cache_contents = get_cache_contents(cache)

    if cache_contents and code in cache_contents:
        return cache_contents.get(code)
    else:
        return None
