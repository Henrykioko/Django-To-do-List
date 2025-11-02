from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReminderListView.as_view(), name='reminder_list'),
    path('new/', views.ReminderCreateView.as_view(), name='reminder_create'),
    path('reminders/<int:pk>/', views.ReminderDetailView.as_view(), name='reminder_detail'),
    path('reminders/<int:pk>/edit/', views.ReminderUpdateView.as_view(), name='reminder_edit'),
    path('reminders/<int:pk>/delete/', views.ReminderDeleteView.as_view(), name='reminder_delete'),

    
]
