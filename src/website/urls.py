from django.contrib import admin
from django.urls import path

from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='website/hello-world.html')),
    path('admin/', admin.site.urls),
]
