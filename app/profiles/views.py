from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView (APIView):
    """Test API view."""
    def get(self, request, format=None):
        """REsturns a list of APIView features."""
        
        an_apiview = [
            '1', '2'
        ]
        
        return Response({'an_apiview': an_apiview})