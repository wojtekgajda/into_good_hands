from django.apps import AppConfig
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

#
# class AccountConfig(AppConfig):
#     name = 'account'


class IntoGoodHandsConfig(AppConfig):
    name = 'into_good_hands'

