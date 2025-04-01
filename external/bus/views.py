import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BusRouteView(APIView):
    def get(self, request):
        from_city = request.query_params.get('from')
        to_city = request.query_params.get('to')

        if not from_city or not to_city:
            return Response({'error': 'from and to parameters are required'}, status=400)

        try:
            external_url = f"https://m97ksfo27c.execute-api.eu-west-1.amazonaws.com/lyuble/bus/search?from={from_city}&to={to_city}"  # Replace with classmate’s actual URL if deployed
            response = requests.get(external_url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
