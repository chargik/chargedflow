from django.shortcuts import render
from django.views.generic import View, FormView
# Create your views here.
from leads.forms import JoinForm

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "pages/home.html", {})

class HomeView(FormView):
    template_name = 'pages/home.html'
    form_class = JoinForm
    success_url = '/'