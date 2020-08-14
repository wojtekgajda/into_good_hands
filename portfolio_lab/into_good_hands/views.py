from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm, RegistrationForm
from into_good_hands.models import Donation, Institution, CustomUser, Category


class IndexView(View):
    def get(self, request):
        bags = Donation.objects.all().aggregate(Sum('quantity'))

        institutions_count = Institution.objects.count()
        foundations = Institution.objects.filter(type='fundacja')
        ngos = Institution.objects.filter(type='organizacja pozarządowa')
        local_collection = Institution.objects.filter(type='zbiórka lokalna')

        return render(request, 'index.html', {'bags': bags,
                                              'institutions_count': institutions_count,
                                              'foundations': foundations,
                                              'ngos': ngos,
                                              'local_collection': local_collection})


class FormView(View):
    def get(self, request):
        if request.user.is_authenticated:
            categories = Category.objects.all()
            institutions = Institution.objects.all()
            user_name = request.user.first_name
            return render(request, 'form.html', {'user_name': user_name,
                                                 'categories': categories,
                                                 'institutions': institutions,})
        else:
            return redirect('login')


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(
            request,
            'login.html',
            {'form': form}
        )

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            messages.error(request, 'Incorrect data!')
            return render(
                request,
                'login.html',
                {'form': form}
            )
        user = authenticate(
            request=request,
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        if user is None:
            messages.error(request, 'User does not exists!')
            return redirect('register')
        login(request, user)
        return redirect('index')


class Register(View):
    def get(self, request):
        form = RegistrationForm()
        return render(
            request,
            'register.html',
            {'form': form}
        )

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if not password == form.cleaned_data['confirmation_password']:
                messages.error(request, 'Passwords are different!')
                return render(
                    request,
                    'register.html',
                    {'form': form}
                )
            if CustomUser.objects.filter(email=email):
                messages.error(request, 'User exists!')
                return render(
                    request,
                    'register.html',
                    {'form': form}
                )
            CustomUser.objects.create_user(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=email,
                password=password,
            )
            return redirect('login')


class Profile(View):
    def get(self,request):
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        ctx = {'first_name':first_name,
               'last_name':last_name,
               'email':email}
        return render(request, 'profil.html', ctx)
