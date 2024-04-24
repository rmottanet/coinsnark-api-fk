import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import unittest
from coinsnark.app.utils.currency_data import get_currency_name

class TestGetCurrencyName(unittest.TestCase):

    def test_get_currency_name_known(self):
        # Testa uma sigla de moeda conhecida
        currency_code = "USD"
        expected_name = "United States Dollar"
        result = get_currency_name(currency_code)
        self.assertEqual(result, expected_name)

    def test_get_currency_name_unknown(self):
        # Testa uma sigla de moeda desconhecida
        currency_code = "XYZ"
        expected_name = "Unknown"
        result = get_currency_name(currency_code)
        self.assertEqual(result, expected_name)

if __name__ == '__main__':
    unittest.main()
