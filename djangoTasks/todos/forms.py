from django.forms import ModelForm, Textarea, TextInput
from .models import TodoModel


class AddTodoForm(ModelForm):
    class Meta:
        model = TodoModel
        fields = ["title", "description", "completed", "deadline"]
        widgets = {
            "description": Textarea(attrs={"cols": 100, "rows": 40}),
            "deadline": TextInput(attrs={"class": "persian-date-picker"}),
        }
        labels = {
            "title": "Title",
            "description": "Description",
            "completed": "Completed",
            "deadline": "Deadline",
        }
        help_texts = {
            "deadline": "Date and time when the task should be finished.",
        }
        error_messages = {
            "title": {
                "max_length": "Title must be less than 100 characters.",
                "required": "Title field is required.",
            },
            "description": {
                "required": "Description field is required.",
            },
            "completed": {
                "required": "Completed field is required.",
            },
            "deadline": {
                "required": "Deadline field is required.",
                "max_value": "Deadline must be in the future.",
            },
        }