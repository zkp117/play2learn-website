from django.urls import path
from .views import CustomPasswordChangeView, MyAccountPageView  # Make sure to import CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("password/change/", CustomPasswordChangeView.as_view(), name="account_change_password"),  # Updated view name
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)