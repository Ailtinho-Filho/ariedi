from django.shortcuts import render
from django.views.generic import TemplateView

from workshops.models import Workshop


class WorkshopDetail(TemplateView):

    template_name = "workshops/workshop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workshop'] = Workshop.objects.first()
        return context
