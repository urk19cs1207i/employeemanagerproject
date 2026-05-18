from django import forms 
from app1.models import AddEmployee
from app1.models import CalenderEvent
from app1.models import AddLatestNews
from app1.models import AddJobOpening
from django.contrib.auth.models import User

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model=AddEmployee
        fields="__all__"

class AddLastestNewsForm(forms.ModelForm):
    class Meta:
        model=AddLatestNews
        fields="__all__"

class CalenderEventForm(forms.ModelForm):
    class Meta:
        model=CalenderEvent 
        fields="__all__"

class AddJobOpeningForm(forms.ModelForm):
    class Meta:
        model=AddJobOpening 
        fields="__all__"

class SignupForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password', 'first_name', 'last_name']