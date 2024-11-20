from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Students

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Name"}),
            "course":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Course"}),
            "dob":forms.DateInput(attrs={"class":"form-control","placeholder":"Enter DOB"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter EmailID"}),
            "mobile":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Number"}),
        }