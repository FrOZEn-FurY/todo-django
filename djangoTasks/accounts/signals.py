from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib import messages


def my_user_logged_in_callback(sender, request, user, **kwargs):
    messages.success(request, "You have successfully logged in.", extra_tags="success")


def my_user_logged_out_callback(sender, request, user, **kwargs):
    messages.success(request, "You have successfully logged out.", extra_tags="success")


def my_user_login_failed_callback(sender, request, credentials, **kwargs):
    messages.error(request, "Invalid username or password.", extra_tags="danger")


user_logged_in.connect(my_user_logged_in_callback)
user_logged_out.connect(my_user_logged_out_callback)
user_login_failed.connect(my_user_login_failed_callback)