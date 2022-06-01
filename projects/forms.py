from django import forms

from projects.models import Project

class register(forms.Form):
    name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=50)
    email = forms.EmailField(label='Email', max_length=255)

class newProj(forms.Form):  
    title = forms.CharField(label='title', max_length=100)
    description = forms.CharField(label='description', max_length=1000)
    technology = forms.CharField(label='technology', max_length=50)
    image = forms.ImageField(max_length=1000000)