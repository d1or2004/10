from django import forms


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=40)
    username = forms.CharField(max_length=59)
    password = forms.CharField(max_length=49)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40)
