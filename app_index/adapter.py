#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import get_adapter as get_account_adapter
from django.urls import reverse
from .models import *

from allauth.account.utils import user_username, user_email, user_field


class ColectivAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """

        data = form.cleaned_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, 'first_name', first_name)
        if last_name:
            user_field(user, 'last_name', last_name)
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()

        route_id = request.session.__getitem__('route_id')
        route = Route.objects.get(pk=route_id)
        route.user = user
        route.save()

        return user


class ColectivSocialAccountAdapter(DefaultSocialAccountAdapter):

    # Create User Profile Here
    def save_user(self, request, sociallogin, form=None):

        u = sociallogin.user
        u.set_unusable_password()
        if form:
            get_account_adapter().save_user(request, u, form)
        else:
            get_account_adapter().populate_username(request, u)
        sociallogin.save(request)
        items = request.session.items()
        print(items)
        for key, value in items:
            print(key)
            print(value)
        route_id = request.session.__getitem__('route_id')
        print(route_id)
        try:
            route = Route.objects.get(pk=route_id)
            route.user = u
            route.save()
        except:
            pass

        return u
