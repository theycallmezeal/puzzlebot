from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tier(models.Model):
	number = models.PositiveSmallIntegerField(unique=True)
	num_to_unlock = models.PositiveSmallIntegerField()

class Puzzle(models.Model):
	number = models.PositiveSmallIntegerField(unique=True)
	tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
	answer = models.CharField(max_length=100)

class SolvedPuzzle(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
	
	class Meta:
		unique_together = ('user', 'puzzle')