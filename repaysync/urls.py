from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import home  # Home view from repaysync/views.py

urlpatterns = [
    path('', home, name='home'),  # Homepage
    path('admin/', admin.site.urls),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('users.urls')),
    path('api/customers/', include('customers.urls')),
    path('api/interactions/', include('interactions.urls')),
    path('api/logs/', include('logs.urls')),  # API logs endpoint
    path('api/loans/', include('loans.urls')),
]
