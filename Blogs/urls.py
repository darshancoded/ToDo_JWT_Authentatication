from django.urls import path 
from .views import Blogview,AllView,BlogUpdateDelete
urlpatterns = [
    path('createblog/',Blogview.as_view(),name='Createblog'),
    path('updateblog/<int:pk>/',BlogUpdateDelete.as_view(),name='Updateblog'),
    path('getblog/',AllView.as_view(),name='get-blog'),
    path('getblog/<int:pk>/',AllView.as_view(),name='get-single-blog'),
    path('delete/<int:pk>/',BlogUpdateDelete.as_view(),name='Delete-blog')
    
]
