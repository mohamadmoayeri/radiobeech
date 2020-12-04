from django.urls import path

from .views import *

from django.conf.urls import url



urlpatterns = [

    path('register',REGISTER,name="register"),

    path('login',LOGIN.as_view(),name="login"),

    path('logout',LOGOUT.as_view(),name="logout"),

    path('reset/password',password_reset_form, name='password_reset_form'),

	path('reset/done/',PASSWORD_RESET_DONE.as_view(), name='password_reset_done'),

	url(r'confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,20}-[0-9A-Za-z]{1,32})/$',PASSWORD_RESET_CONFIRM.as_view(), name='password_reset_confirm'),

	path('confirm/done/',PASSWORD_RESET_COMPLETE.as_view(), name='password_reset_complete'),


]
