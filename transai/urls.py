from django.urls import path
from .views import TranslateView
from .auth_views import RegisterView, ObtainTokenView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('translate/', TranslateView.as_view(), name='translate'),

    path('auth/register/', RegisterView.as_view(), name='register'),

    path('auth/obtaintoken/', ObtainTokenView.as_view(), name='obtaintoken'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
