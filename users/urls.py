from django.urls import path
from .views import RegisterApi, LoginApi, LogoutApi

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='api-register'),
    path('login/', LoginApi.as_view(), name='api-login'),
    path('logout/', LogoutApi.as_view(), name='api-logout'),
]
