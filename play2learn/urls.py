from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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
    path('contact/', include('contact.urls', namespace='contact')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)