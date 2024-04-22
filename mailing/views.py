import random
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission

from mailing import models
from mailing.forms import ClientForm, MailForm, MailingConfigForm
from mailing.runapscheduler import get_cache_for_mailings

from blog.models import Article

# Index app
class IndexView(TemplateView):
    template_name = 'mailing/index.html'
    extra_context = {
        'title': 'Главная',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mail_count'] = get_cache_for_mailings()
        context_data['active_mail_count'] = len(models.MailingConfig.objects.filter(is_active=True))
        context_data['client_count'] = len(models.Client.objects.all())

        if Article.objects.all().count() > 2:
            context_data['object_list'] = random.choices(list(Article.objects.all()), k=3)

        return context_data


def contacts(request):
    context = {
        'title': "Контакты",
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name} ({phone}, {email}): {message}")

    return render(request, 'mailing/contacts.html', context)

# Client models
class ClientListView(LoginRequiredMixin, ListView):
    model = models.Client
    extra_context = {
        'title': 'Ваши клиенты',
    }

    def get_queryset(self, **kwargs):
        if self.request.user.is_superuser:
            return models.Client.objects.all()
        return models.Client.objects.filter(owner=self.request.user)

class ClientDetailView(DetailView):
    model = models.Client

class ClientCreateView(CreateView):
    model = models.Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class ClientUpdateView(UpdateView):
    model = models.Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client')

class ClientDeleteView(DeleteView):
    model = models.Client
    success_url = reverse_lazy('mailing:client')

# Mail models
class MailListView(LoginRequiredMixin, ListView):
    model = models.Mail
    extra_context = {
        'title': 'Сообщения для рассылки',
    }

    def get_queryset(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return models.Mail.objects.all()
        return models.Mail.objects.filter(owner=self.request.user)

class MailDetailView(DetailView):
    model = models.Mail

class MailCreateView(CreateView):
    model = models.Mail
    form_class = MailForm
    success_url = reverse_lazy('mailing:mail') 

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class MailUpdateView(UpdateView):
    model = models.Mail
    form_class = MailForm
    success_url = reverse_lazy('mailing:mail')

class MailDeleteView(DeleteView):
    model = models.Mail
    success_url = reverse_lazy('mailing:mail')

# MailingConfig models
class MailingConfigListView(LoginRequiredMixin, ListView):
    model = models.MailingConfig
    extra_context = {
        'title': "Рассылки",
    }

    def get_queryset(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return models.MailingConfig.objects.all()
        p_view_mail = Permission.objects.get(codename='mailing_config_detail')
        p_change_mail = Permission.objects.get(codename='update_mailing_config')
        p_delete_mail = Permission.objects.get(codename='delete_mailing_config')
        self.request.user.user_permissions.set([p_view_mail, p_change_mail, p_delete_mail])
        return models.MailingConfig.objects.filter(owner=self.request.user)

class MailingConfigDetailView(DetailView):
    model = models.MailingConfig

class MailingConfigCreateView(CreateView):
    model = models.MailingConfig
    form_class = MailingConfigForm
    success_url = reverse_lazy('mailing:mailing_config') 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class MailingConfigUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.MailingConfig
    form_class = MailingConfigForm
    success_url = reverse_lazy('mailing:mailing_config')
    permission_required = 'mailing.change_mail'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

class MailingConfigDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.MailingConfig
    success_url = reverse_lazy('mailing:mailing_config')
    permission_required = 'mailing.delete_mailing_config'

def toogle_activity(request, pk):
    mail_item = get_object_or_404(models.MailingConfig, pk=pk)

    if mail_item.is_active:
        mail_item.is_active = False
    else:
        mail_item.is_active = True
    mail_item.save()

    return redirect('mailing:mailing_config')