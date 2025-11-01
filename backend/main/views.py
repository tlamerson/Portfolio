from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
# Create your views here.

def main_page(request):
    return render(request, 'main/index.html')

def project_page(request):
    return render(request, 'main/projects.html')

def contact_page(request):
    return render(request, 'main/contact.html')

class ExternalRedirectView(RedirectView):
    url = 'https://tylera.pythonanywhere.com/'
    permanent = True

class ExternalRedirectView_2(RedirectView):
    url = 'https://github.com/tlamerson/To-do-Django'
    permanent = True

class ExternalRedirectView_3(RedirectView):
    url = 'https://tylercodes.pythonanywhere.com/'
    permanent = True