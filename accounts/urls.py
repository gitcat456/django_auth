from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, UserProfile

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', UserProfile.as_view(), name='user_profile'),
]