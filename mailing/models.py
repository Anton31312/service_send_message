from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null':True}

class Client(models.Model):

    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', **NULLABLE)
    email = models.EmailField(max_length=254, verbose_name='Электронная почта')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.patronymic}'
    
    class Meta():
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'           

class Mail(models.Model):

    them_mail = models.CharField(max_length=150, verbose_name='Тема письма')
    body_mail = models.TextField(verbose_name='Тело письма', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self) -> str:
        return f'{self.them_mail}'
    
    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

class MailingConfig(models.Model):

    PERIOD_CHOICES = [
        ('per_day', 'раз в день'),
        ('per_week', 'раз в неделю'),
        ('per_month', 'раз в месяц'),
    ]
    STATUS_CHOICES = [
        ('create', 'создана'),
        ('complete', 'завершена'),
        ('extend', 'запущена'),
    ]

    name = models.CharField(max_length=100, verbose_name='Название рассылки', default='Рассылка')
    clients = models.ManyToManyField(Client, verbose_name='Кому (клиенты сервиса)')
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name="Сообщение")
    date_start = models.DateField(verbose_name='Дата начала рассылки', default=timezone.now)
    date_next = models.DateTimeField(verbose_name="следующая дата рассылки",default=timezone.now)
    date_end = models.DateField(verbose_name='Дата окончания рассылки', default=timezone.now)
    start_time = models.TimeField(verbose_name='Время рассылки', default=timezone.now)
    period = models.CharField(max_length=30, choices=PERIOD_CHOICES, verbose_name='Периодичность рассылки',
                              default='per_day')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name='Статус рассылки',
                              default='create')
    is_active = models.BooleanField(default=True, verbose_name='Активация рассылки')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')


    def __str__(self):
        return f'{self.clients} {self.status}'
    
    class Meta:
        verbose_name = 'настройка'
        verbose_name_plural = 'настройки'
        permissions = [
            ("set_is_active", "активация рассылки")
        ]

class TryMailing(models.Model):

    mailing = models.ForeignKey(MailingConfig, on_delete=models.CASCADE, verbose_name='Рассылка', **NULLABLE)
    date_last_try = models.DateTimeField(auto_now=True, verbose_name='Дата последней попытки') 
    status_try = models.CharField(max_length=50, verbose_name='Статус попытки')
    answer_postmail = models.TextField(max_length=500, verbose_name='Ответ почтового сервера', **NULLABLE)

    def __str__(self) -> str:
        return f'{self.status_try}'
    
    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
