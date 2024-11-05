from django.urls import path
from .views import TranslateView, AdminView
from .auth_views import RegisterView, ObtainTokenView, RegisterAdminView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('translate/', TranslateView.as_view(), name='translate'),

    path('auth/register/', RegisterView.as_view(), name='register'),

    path('auth/register/admin', RegisterAdminView.as_view(), name='registeradmin'),

    path('auth/obtaintoken/', ObtainTokenView.as_view(), name='obtaintoken'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('translate/admin', AdminView.as_view(), name='admin'),
]
