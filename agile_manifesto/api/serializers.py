from rest_framework import serializers
from .models import Value, Principle


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ["title", "text"]


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principle
        fields = ["title", "text"]
