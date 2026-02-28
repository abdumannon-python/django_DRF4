from django.urls import path

from .views import *

urlpatterns=[
    path('register/',RegiterView.as_view()),
]