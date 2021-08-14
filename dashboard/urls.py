from django.urls import path
from .views import DashboardHomeView

app_name="dashboard"

urlpatterns = [
    path('',DashboardHomeView.as_view(),name="home")
]
