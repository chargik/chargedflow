from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
# from django.views.generic import View, FormView
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
from leads.forms import JoinForm
from .models import Tours

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "pages/home.html", {})

class HomeView(ListView):
    template_name = 'home.html'
    form_class = JoinForm
    success_url = '/thank-you-page'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        queryset = Tours.objects.all()
        return queryset


class TourDetailView(DetailView):#, CreateView):
    template_name = 'tours/tours_detail.html'
    queryset = Tours.objects.all()
    form_class = JoinForm
    # success_url = '/thank-you-page'

    def get_success_url(self):
        return reverse('tour-detail', kwargs={'slug': self.slug})

    # send_mail(subject, message, from_email, to_list, fail_silently=True)
    # subject = 'Заявка с сайта'
    # message = ''.format(slug, name, telephone, time_now)
    # from_email = settings.EMAIL_HOST_USER
    # to_list = 'travellabminsk@gmail.com'
    # send_mail(subject, message, from_email, to_list, fail_silently=True)