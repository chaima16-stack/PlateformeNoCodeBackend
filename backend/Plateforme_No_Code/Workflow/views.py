from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests

CAMUNDA_API_URL = 'http://localhost:8080/engine-rest'

@api_view(['POST'])
def deploy_bpmn(request):
    file = request.FILES['file']
    response = requests.post(
        f'{CAMUNDA_API_URL}/deployment/create',
        files={'data': file},
        data={'deployment-name': 'example_deployment'}
    )
    return JsonResponse(response.json())

@api_view(['POST'])
def start_process(request, process_definition_key):
    response = requests.post(
        f'{CAMUNDA_API_URL}/process-definition/key/{process_definition_key}/start',
        json=request.data
    )
    return JsonResponse(response.json())
