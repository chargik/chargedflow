from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.urls import reverse
from django.views.generic import View, FormView, ListView, DetailView, CreateView, UpdateView

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


class TourDetailView(DetailView, FormView):#, CreateView):
    template_name = 'tours/tours_detail.html'
    # queryset = Tours.objects.all()
    model = Tours
    form_class = JoinForm
    # success_url = '/thank-you-page'

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        telephone = form.cleaned_data.get("telephone")
        instance = form.save(commit=False)
        instance.save()
        subject = 'Заявка с сайта'
        message = '''Заявка со страницы {0} \n\n
        Имя: {1}\n\n
        Телефон:{2}\n\n'''.format(self.request.path_info, form.cleaned_data['name'], form.cleaned_data['telephone'])
        from_email = settings.EMAIL_HOST_USER
        to_email = ['unklerufus@gmail.com']
        send_mail(subject, message, from_email, to_email, fail_silently=True)
        # return super(TourDetailView, self).form_valid(form)
        return HttpResponseRedirect(self.request.path_info)
        # return HttpResponseRedirect("")


    # def get_success_url(self):
    #     return reverse('tour-detail', kwargs={'slug': self.slug})