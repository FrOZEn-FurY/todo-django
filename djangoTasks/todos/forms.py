from django.forms import ModelForm, Textarea, TextInput, CheckboxInput
from .models import TodoModel


class AddTodoForm(ModelForm):
    class Meta:
        model = TodoModel
        fields = ["title", "description", "completed", "deadline"]
        widgets = {
            "description": Textarea(attrs={"cols": 40, "rows": 15, "class": "form-control",
                                           "style": "resize: none;"}),
            "deadline": TextInput(attrs={"class": "persian-date-picker form-control"}),
            "title": TextInput(attrs={"class": "form-control"}),
            "completed": CheckboxInput(attrs={"class": "form-check-input"}),
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