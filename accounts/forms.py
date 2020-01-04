from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name','last_name')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('first_name','last_name')

class CustomUserUpdateForm(ModelForm):
    class Meta():
        model = CustomUser
        fields = ('first_name', 'last_name')

class CustomUserProfileForm(ModelForm):

    class Meta():
        model = UserProfile
        fields = ('photo', 'bio', 'phone', 'city')
