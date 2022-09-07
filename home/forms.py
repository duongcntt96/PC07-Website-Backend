from django import forms
# import re
# from django.contrib.auth.models import User
from home.models import feedBack

class feedBackForm(forms.Form):

    ten = forms.CharField(label='Họ và tên', max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Đặng Bá Dương', 'class':'form-control'}))
    body = forms.CharField(label="Birthdate",
        widget=forms.TextInput(attrs={'placeholder': '09/02/1996', 'class':'form-control',}))

    def save(self):
        # ten = self.cleaned_data['ten']
        body = self.cleaned_data['body']
        p = feedBack(body=body)
        p.save()