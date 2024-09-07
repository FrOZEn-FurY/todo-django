from django.shortcuts import render, redirect
from django.views import View
from .models import TodoModel
from .forms import AddTodoForm


class ShowTodos(View):
    template_url = "todos/showTodo.html"

    def get(self, request):
        todos = TodoModel.objects.all()
        return render(request, self.template_url, {"todos": todos})


class AddTodo(View):
    template_url = "todos/addTodo.html"

    def get(self, request):
        form = AddTodoForm()
        return render(request, self.template_url, {"form": form})

    def post(self, request):
        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = TodoModel.objects.create(title=form.cleaned_data["title"],
                                            description=form.cleaned_data["description"],
                                            completed=form.cleaned_data["completed"],
                                            deadline=form.cleaned_data["deadline"])
            todo.save()
            return redirect('todos:showTodos')
        return render(request, self.template_url, {"form": form})


class DeleteTodo(View):
    def get(self, request, id):
        todo = TodoModel.objects.get(id=id)
        todo.delete()
        return redirect('todos:showTodos')


class EditTodo(View):
    template_url = 'todos/editTodo.html'

    def get(self, request, id):
        form = AddTodoForm(instance=TodoModel.objects.get(id=id))
        return render(request, self.template_url, {"form": form})

    def post(self, request, id):
        todo = TodoModel.objects.get(id=id)
        form = AddTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:showTodos')
        return render(request, self.template_url, {"form": form})