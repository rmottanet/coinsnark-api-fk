import re

# Função de validação baseada em regex para a sigla da moeda
def validate_currency_code(currency_code):
    pattern = "^[a-zA-Z]{3,4}$"
    return bool(re.match(pattern, currency_code))

# Função de validação de valor convertido
def validate_amount(amount):
    amount_str = str(amount)
    pattern = "^\d+(\.\d+)?$"
    return bool(re.match(pattern, amount_str))
