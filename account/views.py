from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.serializers import UserSerializer
from component.helper.response_helper import SuccessResponse, ErrorResponse

User = get_user_model()

class UserRegister(APIView):

    def post(self, request):
        """
        Register user (Super user) for authentication
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = SuccessResponse("User Registration successful!")
            return Response(response.to_json(), status=status.HTTP_201_CREATED)
        response = ErrorResponse("User Registration unsuccessful!", serializer.errors)
        return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)
