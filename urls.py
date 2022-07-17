from django.urls import path
from .views import PlanViews

urlpatterns = [
    path('plans/', PlanViews.as_view())
]
