from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoModel
from .forms import AddTodoForm
from khayyam import JalaliDatetime


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


class AddTodo(CreateView):
    template_name = "todos/addTodo.html"
    model = TodoModel
    form_class = AddTodoForm
    success_url = '/'


class DeleteTodo(DeleteView):
    model = TodoModel
    success_url = '/'


class EditTodo(UpdateView):
    template_name = 'todos/editTodo.html'
    model = TodoModel
    form_class = AddTodoForm
    success_url = '/'

