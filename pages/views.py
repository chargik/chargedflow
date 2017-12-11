from django.shortcuts import render
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


class TourDetailView(DetailView, CreateView):
    template_name = 'tours/tours_detail.html'
    queryset = Tours.objects.all()
    form_class = JoinForm
    success_url = '/thank-you-page'