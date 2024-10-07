from django.urls import path

from .views import TestEmailView, UserListCreateAPIView, UserMeView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list'),
    path('/me', UserMeView.as_view(), name='user-me'),
    path('/test',TestEmailView.as_view(), name='test-email'),
]
