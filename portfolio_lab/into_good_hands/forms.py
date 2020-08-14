from django import forms




class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='',
        help_text='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    last_name = forms.CharField(
        label='',
        help_text='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    email = forms.CharField(
        label='',
        help_text='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='',
        help_text='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'})
    )
    confirmation_password = forms.CharField(
        label='',
        help_text='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'})
    )


class LoginForm(forms.Form):
    email = forms.CharField(
        label='',
        help_text='',
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='',
        help_text='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
