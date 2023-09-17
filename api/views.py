from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['post'])
def get_access_key(request):
    print('here is the data',request.data)
    return Response('data recieved')
