from django.contrib import admin
from django.urls import path, include
from .views import MyAccountView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    # User Management
    path('account/', include('allauth.urls')),
    path('my-account/', MyAccountView.as_view(), name='my-account'),

    # Local Apps
    path('mathfacts/', include('mathfacts.urls')),
    path('anagramhunt/', include('anagramhunt.urls')),
    path('', include('pages.urls')),
]