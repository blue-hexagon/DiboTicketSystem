from django.views.generic import TemplateView


class FrontPage(TemplateView):
    template_name = "base/frontpage.html"


class HelpPage(TemplateView):
    template_name = "base/helppage.html"


class PrivacyPage(TemplateView):
    template_name = "base/privacypage.html"


class SupportPage(TemplateView):
    template_name = "base/supportpage.html"


class CookiesPolicyPage(TemplateView):
    template_name = "base/about_cookies.html"
