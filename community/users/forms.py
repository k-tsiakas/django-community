from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import CommunityUser

class CommunityUserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta: # edit existing model
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


    def __init__(self,*args,**kwargs):
        super().__init__(*args,*kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

class UserUpdateForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ['username','email']
        help_texts = {
            'username': None,
            'email': None,
        }
        widgets = {
            'username':  forms.TextInput(attrs={'placeholder':'ex:test','autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
        }


class CommunityUserUpdateForm(forms.ModelForm):

    class Meta:
        model = CommunityUser
        fields = ['portfolio','profile_pic']
