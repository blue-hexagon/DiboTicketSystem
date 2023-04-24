from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path, include

from dapp.views.static import FrontPage, HelpPage, SupportPage, PrivacyPage, CookiesPolicyPage

# @formatter:off
""" Admin Site """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]

""" Authentication """
""" https://docs.djangoproject.com/en/4.0/topics/auth/default/#module-django.contrib.auth.views """
urlpatterns += [
    path("accounts/login/",                         LoginView.as_view(),            name="login"),
    path("accounts/logout/",                        LogoutView.as_view(),           name="logout"),
    path("accounts/password_change/",               PasswordChangeView.as_view(),   name="password_change"),
]

""" Business Logic """
urlpatterns += [
    # Main
    path("",            FrontPage.as_view(),      name="frontpage"),
    path("help/",       HelpPage.as_view(),       name="helppage"),
    path("support/",    SupportPage.as_view(),    name="supportpage"),
    path("privacy/",    PrivacyPage.as_view(),    name="privacypage"),
    path("cookies/",    CookiesPolicyPage.as_view(),  name="about-cookies"),

    # Logs
]
# @formatter:on
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
