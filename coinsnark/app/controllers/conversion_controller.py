from flask import Blueprint, request, jsonify
from app.services.conversion_service import convert_currency

# Definindo o blueprint
conversion_bp = Blueprint('conversion', __name__)

# Rota da conversão
@conversion_bp.route('/api/convert', methods=['GET'])
def conversion_ctrl():
	# Parâmetros da solicitação
	from_currency = request.args.get('from')
	to_currency = request.args.get('to')
	amount = float(request.args.get('amount'))
	
	from app import cache
	# Retorna siglas armazenadas no cache
	conversion = convert_currency(cache, from_currency, to_currency, amount)
	if conversion:
		return jsonify(conversion.to_json()), 200
	else:
		return jsonify({"message": "Erro na conversão"}), 400
