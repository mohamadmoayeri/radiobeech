from django.urls import path

from .views import add_personal_information,create_story,EDIT_PROFILE,UPDATE_PERSONAL_INFORMATION,CREATE_PERSONAL_INFORMATION


urlpatterns = [

    path('add_personal_information',add_personal_information,name='add_personal_information'),

    path('create_story',create_story,name='create_story'),

    path('edit_profile/<int:pk>',EDIT_PROFILE.as_view(),name='edit_profile'),

    path('update_personal_information/<int:pk>',UPDATE_PERSONAL_INFORMATION.as_view(),name='update_personal_information'),

    path('create_personal_information/<int:pk>',CREATE_PERSONAL_INFORMATION.as_view(),name='create_personal_information'),


]