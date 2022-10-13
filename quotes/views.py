from django.http import Http404
from rest_framework.generics import get_object_or_404

from quotes.models import Quote
from quotes.serializers import QuoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class QuoteList(APIView):
    def get(self, request):
        quote = Quote.objects.all()
        serializer = QuoteSerializer(quote, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuoteDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Quote, pk=pk)
        serializer = QuoteSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        book = get_object_or_404(Quote, pk=pk)
        serializer = QuoteSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        book = get_object_or_404(Quote, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
