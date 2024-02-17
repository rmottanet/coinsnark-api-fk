from flask import Blueprint, request, jsonify
from app.middleware.validator_mdlwr import CurrencyValidationMiddleware
from app.services.conversion_service import convert_currency
from app.models import ErrorResponse

conversion_bp = Blueprint('conversion', __name__)

@conversion_bp.route('/api/convert', methods=['GET'])
def conversion_ctrl():
    validator = CurrencyValidationMiddleware()
    error = validator.validate_request()

    # if params error response
    if isinstance(error, ErrorResponse):
        return jsonify(error.to_json()), error.status_code

    # params
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount'))

    from app import cache

    conversion = convert_currency(cache, from_currency, to_currency, amount)
    
    # if conversion fail response
    if isinstance(conversion, ErrorResponse):
        return jsonify(conversion.to_json()), 400

    # response
    return jsonify(conversion.to_json()), 200

    # fail response
    error_response = ErrorResponse("An unexpected error occurred during conversion")
    return jsonify(error_response.to_json()), 500
