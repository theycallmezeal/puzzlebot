from django.urls import path
from . import views

urlpatterns = [
	path('puzzle/<slug:puzzle_slug>/', views.puzzle, name='puzzle'),
	path('', views.index, name='index')
]