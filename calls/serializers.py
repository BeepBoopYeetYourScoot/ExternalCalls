from rest_framework_json_api import serializers
from . import models
from .models import Farm
from rest_framework_json_api import relations


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['name', 'location', 'capacity', 'buy_price']
