from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    GenreViewSet,
    GetTokenView,
    SignUpView,
    TitleViewSet,
    UserViewSet
)

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('users', UserViewSet, basename='users')
v1_router.register(r'categories', CategoryViewSet, basename='categories')
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', SignUpView.as_view(), name='sign_up'),
    path('v1/auth/token/', GetTokenView.as_view(), name='get_token'),
]
