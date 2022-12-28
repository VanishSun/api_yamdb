from django.urls import path, include
from rest_framework import DefaultRouter

from .views import UserViewSet

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    # path('v1/auth/signup/', __.as_view(), name='sign_up'),
    # path('v1/auth/token/', __.as_view(), name='get_token'),
]
