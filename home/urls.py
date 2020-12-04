from django.urls import path
from .views import *

urlpatterns = [

    path('',HOME.as_view(),name='home'),

    path('story',STORY.as_view(),name='story'),

    path('profile',PROFILE.as_view(),name='profile'),

    path('his_profile/<slug:user>',HIS_PROFILE.as_view(),name='his_profile'),


]
