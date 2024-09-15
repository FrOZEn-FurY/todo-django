from django.forms import CharField, ModelForm, Textarea, TextInput, CheckboxInput
from .models import TodoModel
from khayyam import JalaliDatetime


class AddTodoForm(ModelForm):
    deadline = CharField(required=True, widget=TextInput(attrs={"class": "persian-date-picker form-control"}),
                         label="Deadline", help_text="Date and time when the task should be finished.")

    class Meta:
        model = TodoModel
        exclude = ["deadline",]
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
            },
        }

    def clean_deadline(self):
        date = self.cleaned_data["deadline"]
        date = JalaliDatetime.strptime(date, "%Y/%m/%d %H:%M:%S").todatetime()
        return date

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.deadline = self.cleaned_data["deadline"]
        if commit:
            instance.save()
        return instance