import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import pytest
from datetime import datetime
from unittest.mock import MagicMock, patch
from coinsnark.app.services.conversion_service import convert_currency
from coinsnark.app.models import ConversionResponse

def test_convert_currency():
    # Mock do cache contendo as taxas de câmbio
    mock_cache = {
        "USD": 1.0,
        "BRL": 5.3,
        "EUR": 0.9
    }

    # Parâmetros de entrada para a conversão
    from_currency = "USD"
    to_currency = "BRL"
    amount = 100

    # Taxas de câmbio simuladas
    from_rate = mock_cache[from_currency]
    to_rate = mock_cache[to_currency]

    # Taxa de câmbio esperada
    expected_exchange_rate = to_rate / from_rate

    # Resultado esperado da conversão
    expected_converted_amount = round(amount * expected_exchange_rate, 2)
    expected_cache_updated = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    expected_conversion_data = {
        "cache_updated": expected_cache_updated,
        "from": from_currency,
        "to": to_currency,
        "converted": expected_converted_amount
    }
    expected_conversion_response = ConversionResponse(expected_conversion_data)

    # Simular obtenção das taxas de câmbio do cache
    with patch('coinsnark.app.services.conversion_service.get_exchange_rate') as mock_get_exchange_rate:
        mock_get_exchange_rate.side_effect = lambda cache, currency: mock_cache[currency]

        # Chamar a função de conversão
        result = convert_currency(mock_cache, from_currency, to_currency, amount)

    # Verificar se a conversão retornou o resultado esperado
    assert result.conversion_data == expected_conversion_data
