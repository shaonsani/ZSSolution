class ResponseModel:
    """
    Custom response helper class for both success and error repsonse
    """
    def __init__(self, message, type, errors=None):
        self.message = message
        self.type = type
        self.errors = errors

    def to_json(self):
        response = {"message": self.message, "type": self.type}
        if self.errors:
            response["errors"] = self.errors
        return response


class SuccessResponse(ResponseModel):
    """
        Custom response helper class for both success
    """
    def __init__(self, message, type="success"):
        super().__init__(message, type)


class ErrorResponse(ResponseModel):
    """
            Custom response helper class for both error, which also return serializer errors
    """
    def __init__(self, message, errors=None, type="failed"):
        super().__init__(message, type, errors)