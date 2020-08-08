from django.contrib import admin
from .models import *

admin.site.register(Tier)
admin.site.register(Puzzle)
admin.site.register(SolvedPuzzle)