from django.urls import path
from crud import views


app_name = 'crud'

urlpatterns = [
    path('', views.index, name='index')
]
