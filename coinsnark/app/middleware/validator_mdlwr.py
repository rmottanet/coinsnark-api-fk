from app.models.error_model import ErrorResponse
from app.utils import validate_currency_code, validate_amount

class CurrencyValidationMiddleware:
    def validate_request(self):
        from flask import request
        # get params
        code_from = request.args.get('from')
        code_to = request.args.get('to')
        amount_str = request.args.get('amount')

        # checkout params
        if not (code_from and code_to and amount_str):
            return ErrorResponse('Missing parameters: from, to, amount')

        if code_from and not validate_currency_code(code_from):
            return ErrorResponse('Invalid currency code (from).')

        if code_to and not validate_currency_code(code_to):
            return ErrorResponse('Invalid currency code (to).')

        if amount_str and not validate_amount(amount_str):
            return ErrorResponse('Invalid amount for conversion.')

        # if ok
        return None
