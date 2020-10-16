import requests
from . import serializers
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Farm
from rest_framework_json_api.parsers import JSONParser
from rest_framework_json_api.renderers import JSONRenderer
import json


class CallViewSet(ModelViewSet):
    serializer_class = serializers.CallSerializer
    queryset = Farm.objects.all()

    def retrieve(self, request, *args, **kwargs):
        url = 'http://localhost:8000/api-access/farms/1'
        r = requests.get(url).json()
        attributes = r['data']['attributes']
        serializer = serializers.CallSerializer(data=attributes)
        if serializer.is_valid():  # Чтобы сохранить распарсенные данные, мне нужно знать полный состав модели,
                                   # включая связи
            serializer.save()
            return redirect('/calls/')
        else:
            return Response(serializer.errors)
