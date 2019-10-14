from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileDetailView, ProfileEditView
from django.views.generic.base import TemplateView
from django_registration.backends.activation.views import ActivationView
from django.conf import settings
from django.conf.urls.static import static
app_name='accounts'

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'),
        name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
        name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),
    path('registration_form/', SignUpView.as_view(),name='django_registration_register'),
    path('register/complete/', TemplateView.as_view(template_name='accounts/registration_complete.html'),
        name='django_registration_complete'),
    path('registration_disallowed/', TemplateView.as_view(template_name='accounts/registration_disallowed.html'),
        name='django_registration_disallowed'),
    path('activate/complete/', TemplateView.as_view(template_name='accounts/activation_complete.html'),
        name='django_registration_activation_complete'),
    path('activate/<activation_key>/', ActivationView.as_view(template_name='accounts/activation_failed.html'),
        name='django_registration_activate'),
    path('profile/', ProfileDetailView, name='profile'),
    path('update_profile/', ProfileEditView, name='update_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
