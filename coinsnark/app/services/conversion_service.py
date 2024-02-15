from datetime import datetime
from app.utils import get_exchange_rate
from app.models import ConversionResponse

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
    # Obter as taxas de câmbio do cache
    from_rate = get_exchange_rate(cache, from_currency)
    to_rate = get_exchange_rate(cache, to_currency)

    # Verificar se as taxas de câmbio foram recuperadas com sucesso
    if from_rate is None or to_rate is None:
        return None

    # Calcular a taxa de câmbio e realizar a conversão
    if from_rate != 0:  # Verificar se a taxa de câmbio não é zero para evitar divisão por zero
        exchange_rate = to_rate / from_rate
        converted_amount = amount * exchange_rate
        
        # Obter o horário do cache, se estiver disponível
        cache_updated = getattr(cache, 'updated_on', datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
        
        # Montar as informações da conversão
        conversion_info = {
			"cache_updated": cache_updated,
			"from": from_currency,
			"to": to_currency,
			"converted": round(converted_amount, 2)  # Arredondar para duas casas decimais
        }
        
        return ConversionResponse(conversion_info)
    else:
        return None
