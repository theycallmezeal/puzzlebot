from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	"""
	if you're not logged in
		display login page
	if you are logged in
		for each tier:
			for each puzzle in said tier:
				determine whether this user has solved it
				display the puzzle
			<hr>
	"""
	return HttpResponse("helo")

def puzzle(request, puzzle_slug):
	"""
		check if the puzzle can be viewed based on the user's highest_solved_tier
		display an error page if not
		404 if the puzzle slug is not found
	"""
	return HttpResponse("you're viewing puzzle " + puzzle_slug)
	
"""
def solve(request):
	get puzzle slug from request
	compare correct answer (stored in db) to user's answer
	if it's correct and if this puzzle hasn't already been solved before:
		create a solvedpuzzle entry
		after saving the solvedpuzzle, if the number of solvedpuzzles at the current tier >= the tier's num_to_unlock:
			update the user's highest_solved_tier
"""