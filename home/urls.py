from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>', views.post, name='post'),
    path('<int:pk>', views.curtiu, name='curtir')
]