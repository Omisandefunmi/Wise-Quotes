from quotes.models import Quote
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import QuoteSerializer
from rest_framework import viewsets
import requests


class GenerateQuote(APIView):

    def get(self, request, format=None):
        results = self.request.query_params.get('text')
        response = {}

        r = requests.get('https://goquotes-api.herokuapp.com/api/v1/random?count=10')

        r_status = 200
       

        if r_status == 200:
            
            data = r.json()
            quotes = data['quotes']

            for q in quotes:
                quote = Quote(
                    text = q['text'],
                    author = q['author']
                )
                quote.save()
            response['status'] = 200
            response['message'] = 'success'
            response['count'] = data

        else:
            response['status'] = 404
            response['message'] = 'error'
            response['credentials'] = {}

        return Response(response)
    

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer







