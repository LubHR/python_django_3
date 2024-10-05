from django.urls import path

from .views import UserListCreateAPIView, UserMeView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list'),
    path('/me', UserMeView.as_view(), name='user-me'),
]
