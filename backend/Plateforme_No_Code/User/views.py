from django.http import JsonResponse
from django.shortcuts import render
from .models import User
from App.models import App, Database
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import requests
from django.contrib.auth import authenticate
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
def generate_jwt_token(user):
        """
            Generate JWT token for the authenticated user.
        """
        app = App.objects.filter(user=user.id_user)
       
    # Define payload for JWT token
        payload = {
        'user_id': user.id_user,

        'exp': datetime.utcnow() + timedelta(days=1)  # Token expiration time (1 day)
    }
    # Generate JWT token using secret key defined in Django settings
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token

class GoogleOAuthLogin(APIView):
    
    @swagger_auto_schema(request_body=AuthentificationSerializer)
    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        if not token:
            return Response({'error': 'No token provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Make a request to Google's tokeninfo endpoint to validate the token
        response = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={token}")
        if response.status_code == 200:
            # Token is valid, extract user information
            user_info = response.json()
            email = user_info.get('email')
            if email:
                # Check if the user already exists
                user, created = User.objects.get_or_create(email=email)
                if created:
                    # If the user is newly created, save the Google client ID
                    user.google_id_client = user_info.get('sub')  
                    user.save()

             
                jwt_token = generate_jwt_token(user)
                return Response({'token': jwt_token})
                
            else:
                return Response({'error': 'Email not provided in token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token has expired'}
    except jwt.InvalidTokenError:
        return {'error': 'Invalid token'}
    
class DecodeTokenView(APIView):
    @swagger_auto_schema(query_serializer=AuthentificationSerializer)
    def get(self, request):
        token = request.query_params.get('token') 
        if not token:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        decoded_token = decode_jwt_token(token)

        return Response(decoded_token)