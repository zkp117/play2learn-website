from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anagramhunt/', include('anagramhunt.urls')),
    path('mathfacts/', include('mathfacts.urls')),
    path('', include('pages.urls')),
]