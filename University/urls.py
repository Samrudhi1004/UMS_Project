from django.urls import path
from University import views

app_name = 'universities'

urlpatterns = [
    path('', views.university_home, name='university_home'),
    path('add/', views.add_view, name='add_university'),
    path('update/<int:pk>/', views.update_view, name='update_university'),
    path('delete/<int:pk>/', views.delete_view, name='delete_university'),
    path('display/', views.display_view, name='display_university'),
    path('display/', views.display_view, name='display_university'),
]