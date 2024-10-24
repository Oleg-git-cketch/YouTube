from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('video/<int:pk>', views.video_page),
    path('category/<int:pk>', views.category_page),
    path('search', views.search)
]