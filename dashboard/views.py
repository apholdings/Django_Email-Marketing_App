from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class DashboardHomeView(TemplateView):
    template_name="dashboard/index.html"