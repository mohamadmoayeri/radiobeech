from django.urls import path
from .views import *

urlpatterns = [

    path('edit/<int:pk>',EDIT_STORY.as_view(),name='edit'),

    path('delete/<int:pk>',DELETE_STORY.as_view(),name='delete'),

  


]