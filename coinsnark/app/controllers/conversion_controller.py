import os
from functools import wraps
from flask import Blueprint, request, jsonify
from coinsnark.app.middleware.validator_mdlwr import CurrencyValidationMiddleware
from coinsnark.app.services.conversion_service import convert_currency
from coinsnark.app.models import ErrorResponse

conversion_bp = Blueprint('conversion', __name__)

@conversion_bp.route('/api/convert', methods=['GET'])
#@token_required
def conversion_ctrl():

    # params
    from_currency = request.args.get('from').upper()
    to_currency = request.args.get('to').upper()
    amount = float(request.args.get('amount'))

    from coinsnark.app import cache

    conversion = convert_currency(cache, from_currency, to_currency, amount)
    
    # if conversion fail response
    if isinstance(conversion, ErrorResponse):
        return jsonify(conversion.to_json()), 400

    # response
    return jsonify(conversion.to_json()), 200

    # fail response
    error_response = ErrorResponse("An unexpected error occurred during conversion")
    return jsonify(error_response.to_json()), 500
