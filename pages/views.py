from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, FormView, ListView, DetailView, CreateView
# Create your views here.
from leads.forms import JoinForm
from .models import Tours

from amocrm import BaseContact, fields

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "pages/home.html", {})

# class HomeView(ListView):
#     template_name = 'home.html'
#     form_class = JoinForm
#     success_url = '/thank-you-page'

#     def get_queryset(self):
#         slug = self.kwargs.get("slug")
#         queryset = Tours.objects.filter(draft=False)
#         return queryset


class BusTour(ListView):
    template_name = 'bus_tour.html'
    queryset = Tours.objects.filter(category='bus')
    # def get_queryset(self):
    #     slug = self.kwargs.get("slug")
    #     queryset = Tours.objects.filter(category='bus')
    #     return queryset
        
class AviaTour(ListView):
    template_name = 'avia_tour.html'
    queryset = Tours.objects.filter(category='avia')
    # def get_queryset(self):
    #     slug = self.kwargs.get("slug")
    #     queryset = Tours.objects.filter(category=avia)
    #     return queryset

class CorpTour(ListView):
    template_name = 'corp_tour.html'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        queryset = Tours.objects.filter(category='corp')
        return queryset

class IndTour(ListView):
    template_name = 'ind_tour.html'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        queryset = Tours.objects.filter(category='ind')
        return queryset       


class TourDetailView(DetailView, SuccessMessageMixin, CreateView):
    template_name = 'tours/tours_detail.html'
    queryset = Tours.objects.all()
    model = Tours
    form_class = JoinForm
    success_url = '/'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(TourDetailView, self).get_context_data(*args, **kwargs)
    #     context['tour_obj'] = Tours.objects.all()
    #     print(context['tour_obj'])
    #     return context

    def get_success_message(self, cleaned_data):
        return "Спасибо за заявку, наш менеджер свяжется с Вами!"

    # def get_success_url(self, *args, **kwargs):
    #     return HttpResponseRedirect(self.request.path_info)


