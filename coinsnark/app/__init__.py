import os
import logging
from flask import Flask, jsonify
from flask_caching import Cache
from app.controllers import main_bp, api_bp, currency_bp, conversion_bp
from app.integrations import BCBQuotes #, ExchangeRates
from app.models import ErrorResponse

# Cache create
cache = Cache()

def create_app(config=None):
	coinsnark = Flask(__name__)
	
	# if no config, use default
	if config:
		coinsnark.config.from_object(config)
	
	# Environment
	coinsnark.config["ENV"] = os.getenv("FLASK_ENV") == "production"
	coinsnark.config["DEBUG"] = os.getenv("FLASK_DEBUG") == "False"
	coinsnark.config["PORT"] = int(os.getenv("PORT", 8000))
	coinsnark.config["EXP"] = os.getenv("EXP")
	coinsnark.config["EXCHANGE_RATES_API_KEY"] = os.getenv("EXCHANGE_RATES_API_KEY")
	
	# Logging
	log_level = os.getenv("LOG_LEVEL", "ERROR")
	logging.basicConfig(level=log_level)
	
	logging.info(f"Valor de EXP: {os.getenv('EXP')}")
	
	# Caching
	coinsnark.config['CACHE_TYPE'] = 'simple'
	cache.init_app(coinsnark)
	
	# Register blueprints	
	coinsnark.register_blueprint(main_bp)
	coinsnark.register_blueprint(api_bp)
	coinsnark.register_blueprint(currency_bp)
	coinsnark.register_blueprint(conversion_bp)

	@coinsnark.errorhandler(404)
	def page_not_found(error):
	    error_response = ErrorResponse('Page not found.', status_code=404)
	    return jsonify(error_response.to_json()), 404
	
	# Integrate BCBQuotes service
	with coinsnark.app_context():
		BCBQuotes.get_bcb_rates_data(cache)
		#ExchangeRates.get_exchange_rates_data(cache)
	
	return coinsnark
