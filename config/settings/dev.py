"""
Local development settings for the pythonsd project.

These settings add some additional debugging features unsuitable for production.
"""

from .base import *  # noqa

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://f719f57fd1934a4eafa36b0418cbd405@o1348685.ingest.sentry.io/6628152",
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)

# Enable Django Debug Toolbar
# https://django-debug-toolbar.readthedocs.io

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE


# Enable template debugging (required for template coverage)
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG
