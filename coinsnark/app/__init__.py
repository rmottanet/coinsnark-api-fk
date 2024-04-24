import os
import logging
from flask import Flask, request, jsonify
from flask_caching import Cache
from flask_cors import CORS
from coinsnark.cache_manager import cache, init_cache
from coinsnark.app.middleware.validator_mdlwr import CurrencyValidationMiddleware
from coinsnark.app.controllers import main_bp, api_bp, currency_bp, conversion_bp
from coinsnark.app.integrations import BCBQuotes, ExchangeRates
from coinsnark.app.models import ErrorResponse


def create_app(config=None):
	coinsnark = Flask(__name__)
	
	CORS(coinsnark, resources={r"/*": {"origins": "*", "methods": "GET"}})
	
	# Se config não for fornecido, use as configurações padrão
	if config:
		coinsnark.config.from_object(config)
	
	# Environment
	coinsnark.config["ENV"] = os.getenv("FLASK_ENV") == "production"
	coinsnark.config["DEBUG"] = os.getenv("FLASK_DEBUG") == "False"
	coinsnark.config["PORT"] = int(os.getenv("PORT", 8000))
	coinsnark.config["COINSNARK_TOKEN"] = os.getenv("COINSNARK_TOKEN")
	coinsnark.config["EXCHANGE_RATES_API_KEY"] = os.getenv("EXCHANGE_RATES_API_KEY")
	
	# Logging
	log_level = os.getenv("LOG_LEVEL", "ERROR")
	logging.basicConfig(level=log_level)
	
	logging.info(f"Valor de EXP: {os.getenv('EXP')}")
		
	init_cache(coinsnark)
	
	# Register blueprints	
	coinsnark.register_blueprint(main_bp)
	coinsnark.register_blueprint(api_bp)
	coinsnark.register_blueprint(currency_bp)
	coinsnark.register_blueprint(conversion_bp)

	@coinsnark.errorhandler(404)
	def page_not_found(error):
	    error_response = ErrorResponse('Page not found.', status_code=404)
	    return jsonify(error_response.to_json()), 404

	def validate_currency_params():
		validator = CurrencyValidationMiddleware()
		error = validator.validate_request()
		
		if isinstance(error, ErrorResponse):
			return jsonify(error.to_json()), error.status_code

	@coinsnark.before_request
	def authenticate_request():
		if request.endpoint and request.endpoint.startswith('conversion.'):
			token = request.headers.get('Authorization')
			expected_token = coinsnark.config.get("COINSNARK_TOKEN")
			if not token or token != f'Bearer {expected_token}':
				return jsonify({'message': 'Unauthorized'}), 401
			error_response = validate_currency_params()
			if error_response:
				return error_response

	def load_exchange_rates():
		# Faça a solicitação para obter os dados de taxas de câmbio
		BCBQuotes.get_bcb_rates_data(cache)
		#ExchangeRates.get_exchange_rates_data(cache)
		# Retorne os dados, que serão armazenados em cache
		return True
    	
	# Integrate BCBQuotes service
	with coinsnark.app_context():
		load_exchange_rates()
	
	return coinsnark
