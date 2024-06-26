# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from coinsnark.app.services.currency_service import get_all_currency_names
from coinsnark.app.models import ErrorResponse

currency_bp = Blueprint('currency', __name__)

@currency_bp.route('/api/currency', methods=["GET"])
def currency_ctrl():

    from coinsnark.app import cache

    response = get_all_currency_names(cache)
    
    # if fails response
    if isinstance(response, ErrorResponse):
        return jsonify({"error": response.error_message}), 400
    elif response is None:
        # anything fails
        error_response = ErrorResponse("An unexpected error occurred")
        return jsonify({"error": error_response.error_message}), 500
    else:
        return jsonify(response.to_json()), 200, {'Content-Type': 'application/json; charset=utf-8'}
