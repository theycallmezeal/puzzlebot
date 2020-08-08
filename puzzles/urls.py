from django.urls import path
from . import views

urlpatterns = [
	path('puzzle/<int:puzzle_num>/', views.puzzle, name='puzzle'),
	path('', views.index, name='index')
]