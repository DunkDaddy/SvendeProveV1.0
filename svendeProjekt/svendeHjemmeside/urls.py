from django.urls import path
from .views import *

urlpatterns = [
    path('',startpage),
    path('logout/', logout),
]
