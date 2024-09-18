from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView as LV, LogoutView as LOV


class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already logged in.", extra_tags="warning")
            return redirect('todos:showTodos')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        user.set_password(form.cleaned_data["password"])
        login(self.request, user)
        messages.success(self.request, "You have successfully registered.", extra_tags="success")
        return super().form_valid(form)


class LoginView(LV):
    template_name = "accounts/login.html"
    form_class = LoginForm
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already logged in.", extra_tags="warning")
            return redirect('todos:showTodos')
        return super().dispatch(request, *args, **kwargs)


class LogoutView(LOV):
    next_page = '/'
    template_name = 'todos/showTodo.html'
