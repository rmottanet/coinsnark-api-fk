import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import pytest
from unittest.mock import MagicMock, patch
from coinsnark.app.services.currency_service import get_all_currency_names
from coinsnark.app.models import CurrencyResponse

def test_get_all_currency_names():
    # Mock do cache contendo siglas e valores
    mock_cache = {
        "USD": "Dollar",
        "BRL": "Real",
        "EUR": "Euro"
    }

    # Chama a função get_all_currency_names com o mock do cache
    with patch('coinsnark.app.services.currency_service.get_cache_contents', return_value=mock_cache):
        # Chama a função e obtém o resultado
        result = get_all_currency_names(mock_cache)

    # Verifica se o resultado contém os nomes humanos esperados dentro do objeto currency_data do CurrencyResponse
    expected_result = {
        "USD": "United States Dollar",
        "BRL": "Brazilian Real",
        "EUR": "Euro"
    }
    assert result.currency_data == expected_result
