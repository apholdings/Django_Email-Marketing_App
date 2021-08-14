
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletter/', include('newsletters.urls', namespace='newsletter')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard'))
]
