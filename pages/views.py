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


class BusTour(ListView):
    template_name = 'bus_tour.html'
    queryset = Tours.objects.filter(category='bus')
        
class AviaTour(ListView):
    template_name = 'avia_tour.html'
    queryset = Tours.objects.filter(category='avia')

class CorpTour(ListView):
    template_name = 'corp_tour.html'
    queryset = Tours.objects.filter(category='corp')


class IndTour(ListView):
    template_name = 'ind_tour.html'
    queryset = Tours.objects.filter(category='ind')
     

class TourDetailView(DetailView, SuccessMessageMixin, CreateView):
    template_name = 'tours/tours_detail.html'
    queryset = Tours.objects.all()
    model = Tours
    form_class = JoinForm
    # success_url = '/thank-you-page'

    def get_success_message(self, cleaned_data):
        return "Спасибо за заявку, наш менеджер свяжется с Вами!"

    # def get_success_url(self, *args, **kwargs):
        # return HttpResponseRedirect(self.request.path_info)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            subject = 'Заявка с сайта'
            message = '''Заявка со страницы {0} \n\n
            Имя: {1}\n\n
            Телефон:{2}\n\n'''.format(self.request.path_info, form.cleaned_data['lead_name'], form.cleaned_data['telephone'])
            from_email = settings.EMAIL_HOST_USER
            to_email = ['unklerufus@gmail.com']
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            return HttpResponseRedirect(self.request.path_info)

        return render(request, self.template_name, {'form': form})

    # def form_valid(self, form):
    #     lead_name = form.cleaned_data.get("lead_name")
    #     telephone = form.cleaned_data.get("telephone")
    #     instance = form.save()
    #     # new_contact = BaseContact(lead_name=lead_name, phone=telephone)
    #     # new_contact.save()
    #     subject = 'Заявка с сайта'
    #     message = '''Заявка со страницы {0} \n\n
    #     Имя: {1}\n\n
    #     Телефон:{2}\n\n'''.format(self.request.path_info, form.cleaned_data['lead_name'], form.cleaned_data['telephone'])
    #     from_email = settings.EMAIL_HOST_USER
    #     to_email = ['unklerufus@gmail.com']
    #     send_mail(subject, message, from_email, to_email, fail_silently=True)
    #     # add amocrm
    #     return HttpResponseRedirect(self.request.path_info)