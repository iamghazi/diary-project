from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm, CustomUserUpdateForm, CustomUserProfileForm
from .models import CustomUser, UserProfile
from django_registration.backends.activation.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect

# Create your views here.

class SignUpView(RegistrationView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('django_registration_complete')
    disallowed_url = reverse_lazy('django_registration_disallowed')
    template_name = 'accounts/registration_form.html'
    email_body_template = 'accounts/activation_email_body.txt'
    email_subject_template = 'accounts/activation_email_subject.txt'

@login_required
def ProfileDetailView(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'accounts/profile.html', {"profile":profile, "user":user,})

@login_required
def ProfileEditView(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method=='POST':
        user_form = CustomUserUpdateForm(request.POST, instance=user)
        profile_form = CustomUserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/accounts/profile/')
    else:
        user_form = CustomUserUpdateForm(instance=user)
        profile_form = CustomUserProfileForm(instance=profile)

    return render(request, 'accounts/update_profile.html',{
    'user_form':user_form, 'profile_form':profile_form,
    })
