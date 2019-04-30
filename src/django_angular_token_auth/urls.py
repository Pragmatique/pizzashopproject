from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token

from django.views.generic import TemplateView

from .views import UserListAPIView



urlpatterns = [
    path('api/v1/auth/login/', obtain_jwt_token),
    path('api/v1/users/', UserListAPIView.as_view()),
    path('api/v1/', TemplateView.as_view(template_name='django_angular_token_auth/index.html')),
]