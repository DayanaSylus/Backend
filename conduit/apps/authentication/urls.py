from django.urls import include, path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
    )

app_name = 'authentication'
urlpatterns = [
    path('Users/register/', RegistrationAPIView.as_view()),
    path('Users/login/', LoginAPIView.as_view()),
    path('Users/view/', UserRetrieveUpdateAPIView.as_view()),
]