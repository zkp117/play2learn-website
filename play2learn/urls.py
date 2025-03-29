from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # User Management
    path('account/', include('users.urls')),
    path('account/', include('allauth.urls')),

    # Local Apps
    path('mathfacts/', include('mathfacts.urls')),
    path('anagramhunt/', include('anagramhunt.urls')),
    path('', include('pages.urls')),
]