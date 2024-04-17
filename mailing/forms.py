from django import forms

from mailing.models import Client, Mail, MailingConfig

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('owner',)

class MailForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mail
        fields = '__all__'
        exclude = ('owner',)

class MailingConfigForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(owner=user)
        self.fields['mail'].queryset = Mail.objects.filter(owner=user)

    class Meta:
        model = MailingConfig
        exclude = ('is_active', )
        fields = '__all__'
        

        widgets = {
            'start_date': forms.DateTimeInput(attrs={'placeholder': 'ДД.ММ.ГГГГ ЧЧ:ММ:СС', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'placeholder': 'ДД.ММ.ГГГГ ЧЧ:ММ:СС', 'type': 'datetime-local'}),
        }