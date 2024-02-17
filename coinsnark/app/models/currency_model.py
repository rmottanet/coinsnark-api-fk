from app.models import ApiResponse

class CurrencyResponse:
    def __init__(self, currency_data):
        self.currency_data = currency_data

    def to_json(self):

        api_response = ApiResponse()
        
        response = {
            "api": api_response.API,
            "api_documentation": api_response.APIDocumentation,
            "currencies": self.currency_data,
            "license": api_response.License,
            "terms_of_use": api_response.TermsOfUse,
            "timestamp": api_response.Timestamp
        }
        
        return response

