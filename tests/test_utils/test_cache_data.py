import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from unittest.mock import MagicMock
import pytest
from coinsnark.app.utils.cache_data import save_data_to_cache, get_cache_contents

def test_save_data_to_cache():
    # Criamos um mock para o cache
    mock_cache = MagicMock()

    # Dados de exemplo a serem salvos no cache
    data_to_save = {'key1': 'value1', 'key2': 'value2'}

    # Chamamos a função que estamos testando
    save_data_to_cache(data_to_save, mock_cache)

    # Verificamos se a função set do cache foi chamada corretamente para cada par chave-valor
    expected_calls = [((k, v), {'timeout': 21600}) for k, v in data_to_save.items()]
    mock_cache.set.assert_has_calls(expected_calls, any_order=True)

def test_get_cache_contents():
    # Criamos um mock para o cache
    mock_cache = MagicMock()

    # Dados de exemplo presentes no cache
    cache_contents = {'key1': 'value1', 'key2': 'value2'}

    # Definimos o comportamento do mock para a função get
    def mock_get(key):
        return cache_contents.get(key, None)

    # Configuramos o mock para retornar valores do cache
    mock_cache.get.side_effect = mock_get

    # Definimos o comportamento do mock para as chaves do cache
    mock_cache.cache._cache.keys.return_value = cache_contents.keys()

    # Chamamos a função que estamos testando
    result = get_cache_contents(mock_cache)

    # Verificamos se a função retorna os valores esperados do cache
    assert result == cache_contents
