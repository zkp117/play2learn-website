from django.urls import path
from .views import DjangoPasswordChangeView, MyAccountPageView, clear_avatar  # Make sure to import CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("password/change/", DjangoPasswordChangeView.as_view(), name="account_change_password"),  # Updated view name
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
    path('avatar/clear/', clear_avatar, name='clear_avatar'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)