from django.urls import path
from . import views

app_name = "todos"
urlpatterns = [
    path("", views.ShowTodos.as_view(), name="showTodos"),
    path("add-todo", views.AddTodo.as_view(), name="addTodo"),
    path("delete-todo/<int:pk>", views.DeleteTodo.as_view(), name="deleteTodo"),
    path('edit-todo/<int:pk>', views.EditTodo.as_view(), name="editTodo"),
]