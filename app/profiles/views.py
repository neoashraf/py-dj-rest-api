from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView (APIView):
    """Test API view."""
    def get(self, request, format=None):
        """Returns a list of APIView features."""
        
        an_apiview = [
            '1', '2'
        ]
        
        return Response({'message':'Hello Dear', an_apiview': an_apiview})