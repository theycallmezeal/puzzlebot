from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("helo")

def puzzle(request, puzzle_slug):
	return HttpResponse("you're viewing puzzle " + puzzle_slug)