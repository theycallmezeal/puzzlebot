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
	
class HighestSolvedTier(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
	
# link up the HighestSolvedTier class to the User class; update HighestSolvedTier whenever its User is updated as well.
@receiver(post_save, sender=User)
def create_highest_solved_tier(sender, instance, created, **kwargs):
	if created:
		HighestSolvedTier.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_highest_solved_tier(sender, instance, **kwargs):
	# User.highest_solved_tier is an automatically generated field.
	instance.highest_solved_tier.save()