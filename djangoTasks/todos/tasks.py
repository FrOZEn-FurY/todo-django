from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from celery import shared_task
from .models import TodoModel
from jalali_date import date2jalali
import datetime


@shared_task()
def schedule_mail():
    for todo in TodoModel.objects.all():
        if todo.deadline.date() == date2jalali(datetime.datetime.now().date()) and todo.completed is False:
            message = render_to_string('e-mail/deadline.html', {'task': todo})
            email = EmailMessage(
                subject=f'Your task {todo.title} is due today!',
                body=message,
                to=[todo.author.email],
            )
            email.send()