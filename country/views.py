from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from component.helper.response_helper import SuccessResponse, ErrorResponse
from country.models import Country
from country.serializers import CountrySerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CountryAPI(APIView):

    def get(self, request):
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')
        if page and limit:
            countries = Country.objects.all()
            paginator = Paginator(countries, limit)
            try:
                countries = paginator.page(page)
            except EmptyPage:
                countries = paginator.page(paginator.num_pages)
            except PageNotAnInteger:
                countries = paginator.page(1)

            serializer = CountrySerializer(countries, many=True)
            response = {
                "data": serializer.data,
                "total_data": paginator.count,
                "current_page": page,
                "last_page": paginator.num_pages
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = ErrorResponse("Page, Limit & Album must be provided!")
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)