from django.urls import path
from . import views

urlpatterns = [
    path('', views.toto_list, name='toto_list'),
    path('add/', views.add_toto, name='add_toto'),  # Ajouter cette ligne
    path('edit/<int:toto_id>/', views.edit_toto, name='edit_toto'),
    path('delete/<int:toto_id>/', views.delete_toto, name='delete_toto'),
]
