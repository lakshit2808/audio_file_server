from django.urls import path, include
from .views import *

urlpatterns = [
    path('' , AudioView.as_view() , name='Home'),
]