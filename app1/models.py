from datetime import date, datetime
from django.db import models
from django.urls import reverse


class Reminder(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=date.today, null=True, blank=True) 
    due_time = models.TimeField(default=datetime.now, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    priority = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reminder_list', args=[str(self.id)])
