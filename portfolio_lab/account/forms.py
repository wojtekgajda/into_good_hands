# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model
# from django import forms
# from django.shortcuts import redirect
# from django.urls import reverse_lazy
#
# from account.models import CustomUser
#
#
# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
#
#         widgets = {
#
#             'first_name': forms.TextInput(attrs={'placeholder': 'Imię'}),
#             'last_name': forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
#             'password1': forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
#             'password2': forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}),
#         }
#
#
# class LoginForm(AuthenticationForm):
#
#     username = forms.EmailField()
#
#     class Meta:
#         model = CustomUser
#         widgets = {
#             'email': forms.TextInput(attrs={'placeholder': 'E-Mail'}),
#         }
#
#
