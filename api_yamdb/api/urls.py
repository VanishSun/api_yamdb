from django.urls import path, include
from rest_framework import DefaultRouter


app_name = 'api'


v1_router = DefaultRouter()
v1_router.register()


urlpatterns = [
    path('', include(v1_router.urls)),

]