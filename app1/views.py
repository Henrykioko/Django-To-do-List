from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Reminder
# Create your views here.

class ReminderListView(ListView):
    model = Reminder
    template_name = "reminder_list.html"

class ReminderDetailView(DetailView):
    model = Reminder
    template_name = "reminder_detail.html"

class ReminderCreateView(CreateView):
    model = Reminder
    template_name = "new.html"
    fields = '__all__'
    success_url = reverse_lazy('reminder_list')

class ReminderUpdateView(UpdateView):
    model = Reminder
    template_name = "reminder_form.html"
    fields = ['title', 'description', 'due_at', 'is_active', 'priority', 'completed']
    success_url = '/reminders/'
  
class ReminderDeleteView(DeleteView):
    model = Reminder
    template_name = "reminder_confirm_delete.html"
    success_url = '/reminders/'

