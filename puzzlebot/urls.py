from django.contrib import admin
from django.urls import include, path
from puzzles import views as puzzle_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('accounts/signup', puzzle_views.signup),
	path('accounts/', include('django.contrib.auth.urls')),
	path('', include('puzzles.urls'))
]
