from django.urls import path

from .views import AboutUsView, HomePageView, MathFactsView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('mathfacts/', MathFactsView.as_view(), name='mathfacts'),
]