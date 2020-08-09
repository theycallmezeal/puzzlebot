from django.urls import path
from . import views

urlpatterns = [
	path('puzzle/<int:puzzle_num>/', views.puzzle, name='puzzle'),
	path('puzzle/solve/<int:puzzle_num>/', views.solve, name='solve'),
	path('', views.index, name='index')
]