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

def puzzle(request, puzzle_num):
	"""
		check if the puzzle can be viewed based on the user's highest_solved_tier
		display an error page if not
		404 if the puzzle num is not found
		if the puzzle number is good...
			grab the html insert from the static files
	"""
	return HttpResponse("you're viewing puzzle " + str(puzzle_num))
	
"""
def solve(request):
	get puzzle num from request
	compare correct answer (stored in db) to user's answer
	if it's correct: (no need to worry about duplicate entries since unique_together is set in SolvedPuzzle)
		create a solvedpuzzle entry
		after saving the solvedpuzzle, if the number of solvedpuzzles at the current tier >= the tier's num_to_unlock:
			update the user's highest_solved_tier
"""