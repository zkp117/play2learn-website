from django.urls import path

from .views import ContactAppView, ContactAppThanksView

app_name = 'contact'
urlpatterns = [
    path('contact-app/', ContactAppView.as_view(), name='app'),
    path('contact-app/thanks/', ContactAppThanksView.as_view(), name='thanks'),
]