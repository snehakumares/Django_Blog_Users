from logging import PlaceHolder
import re
from django.db import models  
from django.forms import fields  
from .models import *  
from django import forms  
  
  
class Registeration(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        super(Registeration, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
        self.fields['profilepicture'].label="Profile Pic "
    type = forms.ChoiceField(choices=(("1","Doctor"),("2","Patient")))
    firstname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'form-control'}))
    lastname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class':'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class':'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control', 'oninput':'passwordvalidate()'}))
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class':'form-control', 'oninput':'passwordvalidate()'}))
    line1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Address', 'class':'form-control'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'City', 'class':'form-control'}))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'State', 'class':'form-control'}))
    pincode = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Pincode', 'class':'form-control'}))

    
    class Meta:   
        model = User
        fields = '__all__'  
    
class newBlog(forms.ModelForm):  
    category = forms.ChoiceField(choices=(("1","Mental Health"),("2","Heart Disease"),("3","Covid19"),("4","Immunization")))
    class Meta:   
        model = Blog
        fields = ['title', 'category', 'summary', 'content', 'image']