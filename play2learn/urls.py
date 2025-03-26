from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # User Management
    path('anagramhunt/', include('anagramhunt.urls')),

    # Local Apps
    path('account/', include('allauth.urls')),
    path('mathfacts/', include('mathfacts.urls')),
    path('', include('pages.urls')),
]