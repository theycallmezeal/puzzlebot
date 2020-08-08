from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	"""
	if you're not logged in
		display login page
	if you are logged in
		for each tier:
			var lowest_locked_tier = some huge number
			look for the tier below
			if the tier below doesn't exist, this tier is unlocked
			if this tier number > lowest_locked_tier, then it's locked
			if the tier below has enough solved, this tier is unlocked
			else this tier is locked; if this tier number < lowest_locked_tier, then lowest_locked_tier = this tier number
			for each puzzle in said tier:
				if the tier is unlocked, determine whether this user has solved it
				display the puzzle
			<hr>
	"""
	return render(request, 'puzzles/index.html', {
	
	})
	
	if request.user.is_authenticated:
		return HttpResponse("logged in as " + request.user.username)
	else:
		return HttpResponse("not logged in")

def puzzle(request, puzzle_num):
	"""
		check if the puzzle can be viewed or not based on the tier below
			if the tier below doesn't exist, this puzzle can be viewed
			if the tier below doesn't have enough puzzles solved, this puzzle cannot be viewed
			if the tier below does have enough puzzles solved, this puzzle can be viewed
		404 if the puzzle num is not found
		if the puzzle number is good...
			grab the html insert from the static files
		maybe: see if a SolvedPuzzle already exists?
	"""
	return HttpResponse("you're viewing puzzle " + str(puzzle_num))
	
"""
def solve(request):
	get puzzle num from request
	compare correct answer (stored in db) to user's answer
	if it's correct: (no need to worry about duplicate entries since unique_together is set in SolvedPuzzle)
		create a solvedpuzzle entry
"""