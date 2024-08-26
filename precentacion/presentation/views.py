from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


# Create your views here.

def index(request):
    return render(request, 'index.html')




def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        try:
            send_mail(
                subject=f"Message from {name}: {subject}",
                message=message + ' Su correo: ' + email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            # Redirige con un indicador de éxito
            return redirect(reverse('contact') + '?success=true')
        except Exception as e:
            print(f"Error sending email: {e}")
            # Redirige con un indicador de error
            return redirect(reverse('contact') + '?success=false')

    success = request.GET.get('success', None)
    return render(request, 'index.html', {'success': success})