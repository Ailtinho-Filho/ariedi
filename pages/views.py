from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from category.models import Category
from projects.models import Project


class Home(TemplateView):

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['projects'] = Project.objects.filter(active=True)
        context['categories'] = Category.objects.all()
        return context


# FIXME: Change to FormView template and place the alert msgs on top of the page
# TODO: Jquery to post message
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = f"Msg from {name}, form in ariedi.com.br"

        send_mail(subject,
                  message,
                  email,
                  ['joaoariedi@gmail.com'],
                  fail_silently=False)
        messages.success(request, 'Thanks, your message is sent successfully.')

    return redirect('home')
