from flask import Blueprint, jsonify
from app.services.currency_service import get_all_currency_names

# Definindo o blueprint
currency_bp = Blueprint('currency', __name__)

# Definindo endpoint para lista de moedas
@currency_bp.route('/api/currency', methods=["GET"])
def currency_ctrl():
    # returns currencies code
    from app import cache
    
    currencies = get_all_currency_names(cache)
    return jsonify(currencies), 200
