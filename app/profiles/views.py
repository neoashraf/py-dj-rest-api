from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets

from . import serializers

# Create your views here.

class HelloApiView (APIView):
    
    """Test API view."""

    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features."""
        
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        
        return Response({'message':'Hello Dear', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name."""
        
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, rquest, pk=None):
        """Handles updating an object."""
        return Response({'method':'put'})
    
    def patch(self, rquest, pk=None):
        """Patch request, only updates fields provided in the request."""
        return Response({'method':'patch'})
    
    def delete(self, rquest, pk=None):
        """Handles deleting an object."""
        return Response({'method':'delete'})
    
    
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""
    
    def list(self, request):
        """Returns a hello message."""
        
        a_viewset = [
            'Uses actions (list, create,retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        
        return Response({'message': 'Hello', 'a_viewset': a_viewset})