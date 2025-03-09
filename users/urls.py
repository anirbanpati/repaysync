from django.urls import path
from .views import UserRegisterView, UserListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('', UserListView.as_view(), name='user_list'),
]
