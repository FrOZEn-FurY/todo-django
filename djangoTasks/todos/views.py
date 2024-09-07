from django.shortcuts import render, redirect
from django.views import View
from .models import TodoModel
from .forms import AddTodoForm
from khayyam import JalaliDatetime


class ShowTodos(View):
    template_url = "todos/showTodo.html"

    def get(self, request):
        todos = TodoModel.objects.all()
        for todo in todos:
            hour, minute, second = todo.deadline.time().hour, todo.deadline.time().minute, todo.deadline.time().second
            minute += 30
            if minute >= 60:
                minute -= 60
                hour += 1
            hour += 3
            if hour >= 24:
                hour -= 24
            todo.deadline = JalaliDatetime(todo.deadline).strftime(f"%Y/%m/%d {hour:02}:{minute:02}:{second:02}")
        return render(request, self.template_url, {"todos": todos})


class AddTodo(View):
    template_url = "todos/addTodo.html"

    def get(self, request):
        form = AddTodoForm()
        return render(request, self.template_url, {"form": form})

    def post(self, request):
        data = {}
        data["title"] = request.POST.get("title")
        data["description"] = request.POST.get("description")
        data["completed"] = request.POST.get("completed")
        data["deadline"] = JalaliDatetime.strptime(request.POST.get("deadline"), "%Y/%m/%d %H:%M:%S").todatetime()
        form = AddTodoForm(data)
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