from django.forms import ModelForm, Textarea, TextInput, CheckboxInput
from .models import TodoModel
from jalali_date.widgets import AdminJalaliDateWidget
from jalali_date.fields import JalaliDateField


class AddTodoForm(ModelForm):
    deadline = JalaliDateField(label="Deadline", widget=AdminJalaliDateWidget,
                               help_text="Make sure that the time you enter is greater than now.", required=True)

    class Meta:
        model = TodoModel
        exclude = ['author',]
        widgets = {
            "description": Textarea(attrs={"cols": 40, "rows": 15, "class": "form-control",
                                           "style": "resize: none;"}),
            "title": TextInput(attrs={"class": "form-control"}),
            "completed": CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "title": "Title",
            "description": "Description",
            "completed": "Completed",
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
            }
        }
