from app.models import ApiResponse

class ErrorResponse:
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        self.api_response = ApiResponse()  # Instanciando o modelo padrão aqui

    def to_json(self):
        return {
            **self.api_response.basic_info(),  # Incluindo informações padrão da API
            "error": {
                "message": self.message,
                "status": self.status_code
            }
        }
