from django.views.generic import CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    
class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_profile'
    login_url = reverse_lazy('login') 
    
    def get_object(self):
        return self.request.user
    