from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets,status

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication

from .serializers import personal_information_serializer,story_serializer

from home.models import story

from profiles.models import personal_information




class api_personal_information(viewsets.ModelViewSet):

    authentication_classes=[TokenAuthentication,]

    queryset=personal_information.objects

    serializer_class=personal_information_serializer

    http_method_names=['get', 'post', 'put', 'delete']

    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(person=self.request.user)




class api_stories(viewsets.ModelViewSet):

    permission_classes=[]

    queryset=story.objects.all()

    serializer_class=story_serializer

    http_method_names=['get']

    #search_fields=['title',]





class api_edit_story(viewsets.ModelViewSet):

    authentication_classes=[TokenAuthentication,]

    permission_classes=[IsAuthenticated,]

    queryset=story.objects

    serializer_class=story_serializer

    http_method_names=['get', 'post', 'put', 'delete']

    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(user=self.request.user)
    







