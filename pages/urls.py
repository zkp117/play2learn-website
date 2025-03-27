from django.urls import path, include

from .views import AboutUsView, HomePageView, MathFactsView, MyAccountView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('math_scorelist/', MathFactsView.as_view(), name='math-scorelist'),
    path('my-account/', MyAccountView.as_view(), name ='my-account'),
]