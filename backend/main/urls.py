from django.urls import path, include
from .views import main_page
from .views import project_page
from .views import contact_page
from .views import ExternalRedirectView
from .views import ExternalRedirectView_2
from .views import ExternalRedirectView_3

urlpatterns = [
    path('', main_page, name="main"),
    path('projects/', project_page, name="project"),
    path('contact/', contact_page, name="contact"),
    path('go/', ExternalRedirectView.as_view(), name='go_external'),
    path('go_2/', ExternalRedirectView_2.as_view(), name="go_external_2"),
    path('go_3/', ExternalRedirectView_3.as_view(), name="go_external_3"),
]
