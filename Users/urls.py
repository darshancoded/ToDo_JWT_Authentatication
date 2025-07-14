from django.urls import path
from .views import RegisterUserAPIView, UserUpdateDeleteAPIView,LoginViewAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', RegisterUserAPIView.as_view(), name='user-list'),            
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('<int:pk>/', RegisterUserAPIView.as_view(), name='user-detail'),  
    path('update/<int:pk>/', UserUpdateDeleteAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserUpdateDeleteAPIView.as_view(), name='user-delete'),
    path('login/', LoginViewAPIView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
