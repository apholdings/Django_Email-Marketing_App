from django.shortcuts import render
from django.views.generic import TemplateView, View
from newsletters.models import Newsletter

# Create your views here.
class DashboardHomeView(TemplateView):
    template_name="dashboard/index.html"


class NewslettersDashboardHomeView(View):
    def get(self, request, *args, **kwargs):
        newsletters=Newsletter.objects.all()

        context={
            'newsletters':newsletters
        }
        return render(request, 'dashboard/list.html', context)