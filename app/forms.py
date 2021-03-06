from django import forms
from .models import Activity
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ('title',)
        
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='')
    last_name = forms.CharField(max_length=30, required=False, help_text='')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields.pop('password2')
        
        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'username', 'password1', )   