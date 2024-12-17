from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'api/posts', PostViewSet, basename='post')

urlpatterns = [
    path('',include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    
   
]

