from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control mt-4','placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class':'form-control mt-4','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email']

        labels = {
            'username':'User Name',
            'email': 'Email',
            'first_name':'First Name',
            'last_name':'Last Name',
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control mt-2','placeholder': 'User Name'}),
            'first_name':forms.TextInput(attrs={'class':'form-control mt-4','placeholder': 'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control mt-4','placeholder': 'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control mt-4','placeholder': 'Email'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(label='User Name',widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control ', 'placeholder':'UserName'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete':'current-password', 'class':'form-control my-4', 'placeholder': 'Password'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title', 'desc',]

        labels ={ 'title':'Title', 'desc':'Description', }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control mt-5', 'placeholder':'Title'}),
            'desc':forms.TextInput(attrs={'class':'form-control mt-5' ,'placeholder':'Description'}),
        }


