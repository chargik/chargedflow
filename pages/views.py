from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from leads.forms import JoinForm
from .models import Tours



def send_join_mail(url, data):
    subject = 'Заявка с сайта'
    message = '''Заявка со страницы {0} \n\n
    Имя: {1}\n\n
    Телефон:{2}\n\n'''.format(url, data['lead_name'], data['telephone'])
    from_email = settings.EMAIL_HOST_USER
    to_email = ['unklerufus@gmail.com']
    send_mail(subject, message, from_email, to_email, fail_silently=False)

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

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

    def get_success_url(self, *args, **kwargs):
        return HttpResponseRedirect(self.request.path_info)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.url_field = self.request.path_info
            instance.save()
            send_join_mail(self.request.path_info, form.cleaned_data)
            return HttpResponseRedirect(self.request.path_info)
        return render(request, self.template_name, {'form': form})