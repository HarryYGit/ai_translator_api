from django.urls import path
from .views import TranslateView
from .auth_views import RegisterView, LoginView

urlpatterns = [
    path('translate/', TranslateView.as_view(), name='translate'),

    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]
