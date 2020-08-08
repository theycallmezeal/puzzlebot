from django.db import models
from django.contrib.auth.models import User

class SolvedPuzzle(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	puzzle = models.PositiveSmallIntegerField()