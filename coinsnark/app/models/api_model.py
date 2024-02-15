from datetime import datetime

class ApiResponse:
    def __init__(self):
        self.API = "CoinSnark"
        self.APIDocumentation = "https://rmottanet.gitbook.io/coinsnark/"
        self.License = "https://raw.githubusercontent.com/rmottanet/coinsnark-api-fk/main/LICENSE"
        self.TermsOfUse = "https://rmottanet.gitbook.io/coinsnark/coin-snark/coin-snak-api-terms-of-use"
        self.Timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    def basic_info(self):
        return {
            "api": self.API,
            "api_documentation": self.APIDocumentation,
            "license": self.License,
            "terms_of_use": self.TermsOfUse,
            "timestamp": self.Timestamp
        }
