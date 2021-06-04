class ResponseModel:
    """
    Custom response helper class for both success and error repsonse
    """
    def __init__(self, message, type):
        self.message = message
        self.type = type

    def to_json(self):
        response = {"message": self.message, "type": self.type}
        return response


class SuccessResponse(ResponseModel):
    """
        Custom response helper class for both success
    """
    def __init__(self, message, type="success"):
        super().__init__(message, type)


class ErrorResponse(ResponseModel):
    """
            Custom response helper class for both error
    """
    def __init__(self, message, type="failed"):
        super().__init__(message, type)