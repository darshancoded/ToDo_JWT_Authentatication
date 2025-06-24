from django.urls import path
from .views import RegisterUser, MainUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('', RegisterUser.as_view(), name='user-list'),            
    path('<int:pk>/', RegisterUser.as_view(), name='user-detail'),  
    path('update/<int:pk>/', MainUser.as_view(), name='user-update'),
    path('delete/<int:pk>/', MainUser.as_view(), name='user-delete'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
