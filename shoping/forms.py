from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20, error_messages={'required':'不能为空'})
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=20, error_messages={'required':'不能为空'})
    email = forms.CharField(required=True, max_length=50, error_messages={'required':'不能为空'})
    password = forms.CharField(required=True, min_length=5, error_messages={'required':'不能为空'})
    confirm_password = forms.CharField(required=True, min_length=5, error_messages={'required':'不能为空'})
    address = forms.CharField(required=True, min_length=200, error_messages={'required':'不能为空'})


