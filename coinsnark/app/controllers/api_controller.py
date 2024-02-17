from flask import Blueprint, jsonify
from app.models import ApiResponse, ErrorResponse

api_bp = Blueprint('api', __name__)

@api_bp.route('/api', methods=["GET"])
def api_info():
    api_response = ApiResponse()
    
    # Verifica se a resposta da API é válida
    if api_response:
        return jsonify(api_response.basic_info()), 200
    elif api_response is None:
        # Se a resposta for None, significa que ocorreu um erro inesperado
        error_response = ErrorResponse("An unexpected error occurred while retrieving information")
        return jsonify({"error": error_response.error_message}), 500
    else:
        # Se houve algum outro tipo de erro, retorna um status HTTP 400
        return jsonify({"message": "error when retrieving information."}), 400
