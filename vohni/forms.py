
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView, ListView
from django.forms import ModelForm
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML
from crispy_forms.bootstrap import FormActions


from .models import Journey, User_Email



class EmailCreateForm(ModelForm):
    journeys = forms.ModelChoiceField(required=True, queryset=Journey.objects.filter(active=True), label='Мандрівка')

    class Meta:
        model = User_Email
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(EmailCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('confirm')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'
        self.helperrender_unmentioned_fields = True

        # add buttons
        self.helper.layout.append(FormActions(
            Div(css_class = self.helper.label_class),
            Submit('add_button', u'Надіслати', css_class="btn btn-info"),
            HTML(u"<a class='btn btn-danger' name='cancel_button' href='{% url 'journeys' %}?status_message=Ви відмінили додавання своїх даних'>Скасувати</a>"),
        ))