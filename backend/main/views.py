from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.

def main_page(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail('The contact form ', 'this is the message', 'noreply@tlamerson.com', ['tlamerson983@gmail.com'])
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'main/index.html',
    {'form': form}
                  )


def project_page(request):
    return render(request, 'main/projects.html')

def contact_page(request):
    return render(request, 'main/contact.html')

def project_full_page(request):
    return render(request, 'main/projects-full.html')


class ExternalRedirectView(RedirectView):
    url = 'https://tylera.pythonanywhere.com/'
    permanent = True

class ExternalRedirectView_2(RedirectView):
    url = 'https://github.com/tlamerson/To-do-Django'
    permanent = True

class ExternalRedirectView_3(RedirectView):
    url = 'https://tylercodes.pythonanywhere.com/'
    permanent = True