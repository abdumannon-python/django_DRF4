from django.urls import path
from .views import *

urlpatterns={
    path('create/',ProductCreate.as_view()),
    path('update/',ProductUdate.as_view()),
    path('delete/',ProductDelete.as_view())

}