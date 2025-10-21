from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mark_done/<int:habit_id>/', views.mark_done, name='mark_done'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
]
