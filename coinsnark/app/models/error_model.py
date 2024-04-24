from coinsnark.app.models import ApiResponse

class ErrorResponse:
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        self.api_response = ApiResponse()

    def to_json(self):
        return {
            **self.api_response.basic_info(),
            "error": {
                "message": self.message,
                "status": self.status_code
            }
        }
