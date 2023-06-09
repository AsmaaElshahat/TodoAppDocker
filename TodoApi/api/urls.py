from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path('add/', views.add_data),
    path('update/<int:pk>', views.update_data),
    path('delete/<int:pk>', views.delete_data)
]
