# coinsnark/tests/test_utils/test_requests.py
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
import requests
from unittest.mock import MagicMock, patch
from coinsnark.app.utils.requests import fetch_data

@patch('coinsnark.app.utils.requests.requests.get')
def test_fetch_data_error(mock_get):
    # Define uma URL de teste
    test_url = 'http://example.com'
    
    # Configure o comportamento do mock para simular uma exceção HTTPError
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError('Test error')
    mock_get.return_value = mock_response
    
    # Chame a função fetch_data com a URL de teste e verifique se uma exceção é levantada
    with pytest.raises(RuntimeError):
        fetch_data(test_url)
    
    # Verifique se a função requests.get foi chamada com a URL correta pelo menos uma vez
    mock_get.assert_any_call(test_url)
