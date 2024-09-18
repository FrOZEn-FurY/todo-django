import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoTasks.settings')

app = Celery('djangoTasks')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'send_email_for_deadlines_crontab': {
        'task': 'todos.tasks.schedule_mail',
        'schedule': crontab(hour="0", minute="0")
    }
}