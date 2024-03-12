from django.urls import path
from .views import record_form

urlpatterns = [
    path('record/', record_form, name='record_form'),
]
