from django.urls import path

from mailing.apps import MailingConfig
from mailing import views

app_name = MailingConfig.name

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('contacts/', views.contacts, name='contacts'),

     path('client/', views.ClientListView.as_view(), name='client'),
     path('client/view/<int:pk>', views.ClientDetailView.as_view(), name='client_detail'),
     path('client/create/', views.ClientCreateView.as_view(), name='create_client'),
     path('client/edit/<int:pk>/', views.ClientUpdateView.as_view(), name='update_client'),
     path('client/delete/<int:pk>/', views.ClientDeleteView.as_view(), name='delete_client'),

     path('mail/', views.MailListView.as_view(), name='mail'),
     path('mail/view/<int:pk>', views.MailDetailView.as_view(), name='mail_detail'),
     path('mail/create/', views.MailCreateView.as_view(), name='create_mail'),
     path('mail/edit/<int:pk>/', views.MailUpdateView.as_view(), name='update_mail'),
     path('mail/delete/<int:pk>/', views.MailDeleteView.as_view(), name='delete_mail'),

     path('mailing_config/', views.MailingConfigListView.as_view(), name='mailing_config'),
    path('mailing_config/view/<int:pk>/', views.MailingConfigDetailView.as_view(), name='mailing_config_detail'),
    path('mailing_config/create/', views.MailingConfigCreateView.as_view(), name='create_mailing_config'),
    path('mailing_config/edit/<int:pk>/', views.MailingConfigUpdateView.as_view(), name='update_mailing_config'),
    path('mailing_config/delete/<int:pk>/', views.MailingConfigDeleteView.as_view(), name='delete_mailing_config'),
    path('mailing_config/activity/<int:pk>/', views.toogle_activity, name='toogle_activity'),
]