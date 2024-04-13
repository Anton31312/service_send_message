from django.contrib import admin

from mailing import models

@admin.register(models.Client)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic', 'comment', )
    search_fields = ('last_name', 'first_name',)

@admin.register(models.Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'them_mail', 'body_mail', )
    search_fields = ('them_mail', 'body_mail',)    
    list_filter = ('them_mail',)

@admin.register(models.MailingConfig)
class MailingConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'date_start', 'date_end', 'start_time', 'period', 'status', 'is_active',)
    search_fields = ('mail',)    
    list_filter = ('is_active',)


@admin.register(models.TryMailing)
class TryMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'mailing', 'date_last_try', 'status_try', 'answer_postmail',)
