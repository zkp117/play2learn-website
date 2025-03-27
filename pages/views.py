from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class MathFactsView(TemplateView):
    template_name = 'pages/math_scorelist.html'

class MyAccountView(TemplateView):
    template_name = "account/my_account.html" 