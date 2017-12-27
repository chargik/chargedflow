"""chargedflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
# from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from leads.api.views import JoinCreateAPIView
from pages.views import TourDetailView, BusTour, AviaTour, CorpTour, IndTour


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('thank-you-page/', TemplateView.as_view(template_name='thank-you-page.html'), name='thank-you-page'),
    path('bus-tour-list/', BusTour.as_view(), name='bus-tour-list'),
    path('avia-tour-list/', AviaTour.as_view(), name='avia-tour-list'),
    path('corp-tour-list/', CorpTour.as_view(), name='corp-tour-list'),
    path('ind-tour-list/', IndTour.as_view(), name='ind-tour-list'),
    re_path(r'^api/form/join/$', JoinCreateAPIView.as_view(), name='form-join'),
    re_path(r'(?P<slug>[\w-]+)/$', TourDetailView.as_view(), name='tours-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# r'^(?P<slug>[\w-]+)/$'
