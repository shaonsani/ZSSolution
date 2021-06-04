from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from component.helper.response_helper import SuccessResponse, ErrorResponse
from country.models import Country, State, Address
from country.serializers import CountrySerializer, StateSerializer, AddressSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


class CountryAPI(APIView):

    def get(self, request):
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')
        name = request.query_params.get('name')
        code = request.query_params.get('code')
        q = Q()
        if page and limit:
            if name:
                q &= Q(name=name)
            if code:
                q &= Q(code=code)
            countries = Country.objects.filter(q)
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
            response = ErrorResponse("Page, Limit must be provided!")
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)


class StateAPI(APIView):

    def get(self, request):
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')
        name = request.query_params.get('name')
        q = Q()
        if page and limit:
            if name:
                q &= Q(name=name)
            states = State.objects.filter(q)
            paginator = Paginator(states, limit)
            try:
                states = paginator.page(page)
            except EmptyPage:
                states = paginator.page(paginator.num_pages)
            except PageNotAnInteger:
                states = paginator.page(1)

            serializer = StateSerializer(states, many=True)
            response = {
                "data": serializer.data,
                "total_data": paginator.count,
                "current_page": page,
                "last_page": paginator.num_pages
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = ErrorResponse("Page, Limit must be provided!")
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)


class AddressAPI(APIView):

    def get(self, request):
        page = request.query_params.get('page')
        limit = request.query_params.get('limit')
        house_number = request.query_params.get('house_number')
        road_number = request.query_params.get('road_number')
        q = Q()
        if page and limit:
            if house_number:
                q &= Q(house_number=house_number)
            if road_number:
                q &= Q(road_number=road_number)
            address_list = Address.objects.filter(q)
            paginator = Paginator(address_list, limit)
            try:
                address_list = paginator.page(page)
            except EmptyPage:
                address_list = paginator.page(paginator.num_pages)
            except PageNotAnInteger:
                address_list = paginator.page(1)

            serializer = AddressSerializer(address_list, many=True)
            response = {
                "data": serializer.data,
                "total_data": paginator.count,
                "current_page": page,
                "last_page": paginator.num_pages
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = ErrorResponse("Page, Limit must be provided!")
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)
