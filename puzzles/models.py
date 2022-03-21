from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tier(models.Model):
	number = models.PositiveSmallIntegerField(primary_key=True)
	num_to_unlock = models.PositiveSmallIntegerField()
	
	def __str__(self):
		return 'Tier ' + str(self.number) + ' (' + str(self.num_to_unlock) + ' to unlock)'

class Puzzle(models.Model):
	number = models.PositiveSmallIntegerField(primary_key=True)
	tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
	answer = models.CharField(max_length=100)
	
	def __str__(self):
		return 'Puzzle ' + str(self.number) + ' (Tier ' + str(self.tier.number) + '; answer: ' + self.answer + ')'

class SolvedPuzzle(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.user.username + " solved puzzle " + str(self.puzzle.number)
	
	class Meta:
		unique_together = ('user', 'puzzle')