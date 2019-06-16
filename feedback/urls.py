from django.urls import path

from feedback.views import FeedbackView

urlpatterns = \
    [
        path('ajax<url>', FeedbackView.as_view(), name='feedback'),
    ]

# vim: et sw=4 sts=4
