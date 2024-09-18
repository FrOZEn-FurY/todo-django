from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoModel
from .forms import AddTodoForm
from khayyam import JalaliDatetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class ShowTodos(ListView):
    template_name = "todos/showTodo.html"
    model = TodoModel
    context_object_name = "todos"

    def get_context_data(self, *, object_list=None, **kwargs):
        todos = super().get_context_data()
        for todo in todos["object_list"]:
            hour, minute, second = todo.deadline.time().hour, todo.deadline.time().minute, todo.deadline.time().second
            minute += 30
            if minute >= 60:
                minute -= 60
                hour += 1
            hour += 3
            if hour >= 24:
                hour -= 24
            todo.deadline = JalaliDatetime(todo.deadline).strftime(f"%Y/%m/%d {hour:02}:{minute:02}:{second:02}")
        todos["object_list"] = sorted(todos["object_list"], key=lambda todo: todo.deadline)
        return todos


class AddTodo(LoginRequiredMixin, CreateView):
    template_name = "todos/addTodo.html"
    model = TodoModel
    form_class = AddTodoForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteTodo(LoginRequiredMixin, DeleteView):
    model = TodoModel
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        id = kwargs['pk']
        if TodoModel.objects.get(id=id).author.username != request.user.username:
            messages.warning(request, "You can't delete a todo that is not yours!", extra_tags='warning')
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


class EditTodo(LoginRequiredMixin, UpdateView):
    template_name = 'todos/editTodo.html'
    model = TodoModel
    form_class = AddTodoForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        id = kwargs['pk']
        if TodoModel.objects.get(id=id).author.username != request.user.username:
            messages.warning(request, "You can't edit a todo that is not yours!", extra_tags='warning')
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

