from django.urls import path
from crud import views


app_name = 'crud'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create_user'),
    path('edit/<int:person_id>/', views.edit, name='edit_user'),
    path('delete/<int:person_id>/', views.delete, name='delete_user'),
]
