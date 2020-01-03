from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic.base import TemplateView


class Home(TemplateView):

    template_name = "pages/home.html"


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

