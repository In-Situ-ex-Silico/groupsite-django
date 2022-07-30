from django.urls import path
from django.urls import re_path
from django.views import generic

from .views import HomePageView, PythonPageView, MlPageView, BioPageView


urlpatterns = [
    path(r"", HomePageView.as_view(template_name="pythonsd/index.html"), name="index"),
    path(
        r"code-of-conduct/",
        generic.TemplateView.as_view(template_name="pythonsd/code-of-conduct.html"),
        name="code-of-conduct",
    ),
    path(
        r"denverpython/",
        PythonPageView.as_view(template_name="pythonsd/python-group.html"),
        name="denverpython",
    ),
    path(
        r"denverml/",
        MlPageView.as_view(template_name="pythonsd/data-science-group.html"),
        name="denverml",
    ),
    path(
        r"denverbiology/",
        BioPageView.as_view(template_name="pythonsd/biology-group.html"),
        name="denverbiology",
    ),
    path(
        r"remotework/",
        BioPageView.as_view(template_name="pythonsd/remotework.html"),
        name="remotework",
    ),
]

# These redirects handle redirecting URLs from the old static site to the new Django site
redirects = [
    re_path(
        r"^coc/?$",
        generic.RedirectView.as_view(url="/code-of-conduct/", permanent=False),
    ),
    path(
        r"pages/code-of-conduct.html",
        generic.RedirectView.as_view(url="/code-of-conduct/", permanent=False),
    ),
    # These pages were removed when we transitioned to the old GitHub pages based site
    path(r"index.html", generic.RedirectView.as_view(url="/", permanent=False)),
    path(
        r"pages/chat-room.html",
        generic.RedirectView.as_view(url="/#slack-channel", permanent=False),
    ),
    path(
        r"pages/workshops.html",
        generic.RedirectView.as_view(url="/", permanent=False),
    ),
    path(
        r"pages/getting-started.html",
        generic.RedirectView.as_view(url="/", permanent=False),
    ),
    path(
        r"pages/job-posting-guidelines.html",
        generic.RedirectView.as_view(url="/", permanent=False),
    ),
]

urlpatterns += redirects
