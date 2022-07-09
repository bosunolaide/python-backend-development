from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from links.models import Link
from links.serializers import LinkSerializer

# Create your views here.

class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer
    
class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

