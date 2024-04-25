# -*- coding: utf-8 -*-
from coinsnark.app.models import ApiResponse

class ConversionResponse:
    def __init__(self, conversion_data):
        self.conversion_data = conversion_data

    def to_json(self):

        api_response = ApiResponse()
        
        response = {
            "api": api_response.API,
            "api_documentation": api_response.APIDocumentation,
            "conversion": self.conversion_data,
            "license": api_response.License,
            "terms_of_use": api_response.TermsOfUse,
            "timestamp": api_response.Timestamp
        }
        
        return response
