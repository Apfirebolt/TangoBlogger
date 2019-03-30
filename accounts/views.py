from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import User
from .forms import RegisterForm
from django.views.generic import CreateView, UpdateView, FormView, DetailView, View, ListView, TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import JsonResponse, Http404
from TangoBlogger import settings
from django.core.exceptions import ValidationError


class Dashboard(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'

    def get(self, request, *args, **kwargs):
        user_object = User.objects.get(pk=request.user.id)
        return render(request, self.template_name, {'object': user_object})


class Register(SuccessMessageMixin, FormView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()

        messages.add_message(self.request, messages.INFO, 'You have successfully registered, Please login to continue!')
        return HttpResponseRedirect(reverse('accounts:login'))

    def form_invalid(self, form):
        return render(self.request, 'accounts/register.html', {'form': form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

        else:
            messages.warning(request, 'Invalid login credentials supplied. Please try to login again.')
            return HttpResponseRedirect(reverse('home'))

    else:
        return render(request, 'accounts/login.html', {})


class AccountSettings(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'profile_image']
    template_name_suffix = '_update_form'

    # Implements security so that only data for the given user is accessible.
    def get_queryset(self):
        queryset = super(AccountSettings, self).get_queryset()
        return queryset.filter(username=self.request.user)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Your Account Settings were updated successfully!')
        return reverse('accounts:dashboard')
