import os
from  celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graphics.settings')

app = Celery('graphics')
app.config_from_object('django.conf:settings',namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y