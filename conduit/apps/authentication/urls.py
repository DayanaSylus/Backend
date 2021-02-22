from django.urls import include, path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
    )

app_name = 'authentication'
urlpatterns = [
    path('users/register/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('user/view/', UserRetrieveUpdateAPIView.as_view()),
]