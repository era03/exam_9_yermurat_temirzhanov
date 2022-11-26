from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from accounts.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User



class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('pictures')
        return next_url