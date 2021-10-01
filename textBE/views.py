from django.http import JsonResponse
from django.shortcuts import render
from django.http.request import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .serializers import jsondocSerializer
from .models import jsondoc

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = jsondoc.objects.all()
        serializer = jsondocSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = jsondocSerializer(data=data)
        if serializer.is_valid():
            file = open("Jsonfile.json", "w")
            file.write(f'{data}')
            file.close()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)