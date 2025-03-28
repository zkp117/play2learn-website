from django.urls import path
from .views import CustomPasswordChangeView, MyAccountPageView, EmailConfirmationView

urlpatterns = [
    path("password/change/", CustomPasswordChangeView.as_view(),name="account_change_password"
    ),
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
    path('account/confirm-email/<str:key>/', EmailConfirmationView.as_view(), name='account_confirm_email'),
]