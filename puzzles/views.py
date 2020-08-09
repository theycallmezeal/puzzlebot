from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import *

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def index(request):
	if not request.user.is_authenticated:
		return render(request, 'puzzles/index.html', {})

	# creates a dictionary where the key is the tier's number
	# and the value is the tier itself, plus some per-user information
	# about that tier. necessary to store the tiers by their number
	# in order to be able to look up tiers by number in the sections below.
	tier_info = {}
	tiers = Tier.objects.all()
	for tier in tiers:
		tier_info[str(tier.number)] = {
			'tier': tier,
			'user_solved_num': SolvedPuzzle.objects.filter(user_id=request.user.id, puzzle__tier__number=tier.number).count(),
			'puzzles': []
		}
	
	# determine whether tiers are locked or unlocked by looking at the tier below.
	# if the tier below doesn't exist, this tier is unlocked.
	# if the tier below has enough solved, this tier is unlocked.
	# if the tier below doesn't have enough solved, this tier is locked.
	for tier_num in tier_info:
		locked = True
		tier_below_num = str(int(tier_num) - 1)
		if tier_below_num not in tier_info:
			locked = False
		else:
			puzzles_required = tier_info[tier_below_num]['tier'].num_to_unlock
			puzzles_solved = tier_info[tier_below_num]['user_solved_num']
			if puzzles_solved >= puzzles_required:
				locked = False
		tier_info[tier_num]['locked'] = locked
	
	# create a list of all the puzzle numbers that this user has solved.
	solved_puzzles = []
	for solved_puzzle in SolvedPuzzle.objects.filter(user_id=request.user.id):
		solved_puzzles.append(solved_puzzle.puzzle.number)
	
	# grab all puzzles.
	# create dictionaries of puzzle number and whether or not it's solved, unsolved, or locked
	# and add these dictionaries to the tier_info.
	for puzzle in Puzzle.objects.all().order_by('number'):
		puzzle_num = str(puzzle.tier.number)
		puzzle_list = tier_info[puzzle_num]['puzzles']
		puzzle_list.append({
			'puzzle_num': puzzle.number,
			'solved': 'Solved' if (puzzle.number in solved_puzzles) else 'Unsolved'
		})
	
	return render(request, 'puzzles/index.html', {
		'tier_info': tier_info.values() # don't need the key numbers any more
	})
		

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
	if not request.user.is_authenticated:
		return render(request, 'puzzles/puzzle_not_logged_in.html', {})
		
	return render(request, 'puzzles/puzzle.html', {})
	
"""
def solve(request):
	get puzzle num from request
	compare correct answer (stored in db) to user's answer
	if it's correct: (no need to worry about duplicate entries since unique_together is set in SolvedPuzzle)
		create a solvedpuzzle entry
"""