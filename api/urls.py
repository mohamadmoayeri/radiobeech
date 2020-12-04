from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import api_personal_information,api_stories,api_edit_story

router=DefaultRouter()

router.register('personal_information',api_personal_information,basename='api_personal_information')

router.register('story',api_stories,basename='api_story')

router.register('edit_story',api_edit_story,basename='edit_api_story')


urlpatterns = [
    
]

urlpatterns += router.urls