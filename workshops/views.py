from django.shortcuts import render
from django.views.generic import TemplateView

from workshops.models import Workshop, WorkshopImage


class WorkshopDetail(TemplateView):

    template_name = "workshops/workshop.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['workshop'] = Workshop.objects.first()
        context['workshop_images'] = WorkshopImage.objects.filter(workshop_id=context['workshop'].id)
        return context
