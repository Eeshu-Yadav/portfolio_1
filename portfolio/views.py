from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Portfolio, LegSettings
from .serializers import PortfolioSerializer, LegSettingsSerializer
import pandas as pd

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class LegSettingsViewSet(viewsets.ModelViewSet):
    queryset = LegSettings.objects.all()
    serializer_class = LegSettingsSerializer

def prog():
    portfolios = Portfolio.objects.prefetch_related('leg_settings').all()
    portfolio_df = []

    for portfolio in portfolios:
        portfolio_settings = {
            'name': portfolio.name,
            'expiry': portfolio.expiry,
            'premium_gap': portfolio.premium_gap,
            'start': portfolio.start,
            'end': portfolio.end,
            'target': portfolio.target,
            'stop_loss': portfolio.stop_loss,
        }
        legs_settings = list(portfolio.leg_settings.all().values())

        portfolio_settings['leg_settings'] = legs_settings
        start_time = pd.to_timedelta(portfolio.start.strftime("%H:%M:%S"))
        end_time = pd.to_timedelta(portfolio.end.strftime("%H:%M:%S"))

        portfolio_settings['start_time'] = start_time
        portfolio_settings['end_time'] = end_time
        portfolio_settings['leg_settings'] = legs_settings

        print(f"{portfolio.name}")
        portfolio_df.append(pd.DataFrame(portfolio_settings))

    return pd.concat(portfolio_df, ignore_index=True)

class PortfolioProgView(APIView):
    def get(self, request, format=None):
        portfolio_df = prog()
        portfolio_json = portfolio_df.to_json(orient='records')
        return Response(portfolio_json)
