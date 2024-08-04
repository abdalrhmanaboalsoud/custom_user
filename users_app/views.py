from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import login
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
    # def form_valid(self, form):
    # # Optionally log in the user immediately after registration
    #     user = form.save()
    #     login(self.request, user)  # Automatically log in the user after sign-up
    #     return super().form_valid(form)