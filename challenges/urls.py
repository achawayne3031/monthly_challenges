
from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.index),
    # path("march", views.march),
    path("", views.index),
    path("<int:month>", views.monthly_challange_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
    
]
