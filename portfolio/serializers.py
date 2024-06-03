from rest_framework import serializers
from .models import Portfolio, LegSettings

class LegSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegSettings
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    leg_settings = LegSettingsSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = '__all__'
