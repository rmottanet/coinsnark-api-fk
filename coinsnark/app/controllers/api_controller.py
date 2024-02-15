from flask import Blueprint, jsonify
from app.models.api_model import ApiResponse

# Definindo o blueprint
api_bp = Blueprint('api', __name__)

# Rota da api
@api_bp.route('/api')
def api_info():
	response = ApiResponse()
	return jsonify(response.basic_info()), 200
