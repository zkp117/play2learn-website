from django.urls import path

from .views import ContactAppView, ContactAppThanksView

app_name = 'contact'
urlpatterns = [
    path('contact_us/', ContactAppView.as_view(), name='app'),
    path('contact_us/thanks/', ContactAppThanksView.as_view(), name='thanks'),
]