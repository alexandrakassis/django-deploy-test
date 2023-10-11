from django.urls import path
from .views import CycleView

urlpatterns = [
    path('home', CycleView.as_view()),
]
