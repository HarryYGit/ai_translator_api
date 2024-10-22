from django.urls import path
from .views import TranslateView, TestConnection
# from .auth_views import RegisterView, LoginView
from .auth_views import RegisterView, ObtainTokenView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('translate/', TranslateView.as_view(), name='translate'),

    path('test/', TestConnection.as_view(), name='test'),

    path('auth/register/', RegisterView.as_view(), name='register'),
    # path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/obtaintoken/', ObtainTokenView.as_view(), name='obtaintoken'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
