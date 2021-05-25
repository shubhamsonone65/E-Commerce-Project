from django import forms

class signup(forms.Form):
    name=forms.forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phone_no=forms.IntegerField(required=True)
    pass1=forms.PasswordInput()
    pass2=forms.PasswordInput()