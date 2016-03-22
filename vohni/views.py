# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView
from django.forms import ModelForm


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML
from crispy_forms.bootstrap import FormActions


from .models import Journey, User_Email


# Create your views here.
def main_page(request):
    journeys = Journey.objects.all()
    order_by = request.GET.get('order_by', 'end_date')
    journeys = journeys.order_by(order_by).filter()[:2]

    return render(request, 'vohni/index.html', {'journeys': journeys})


def journeys(request):

    journeys = Journey.objects.all()
    return render(request, 'vohni/journey_list.html', {'journeys': journeys})

def blog(request):
    return render(request, 'vohni/blog.html', {})

def team(request):
    return render(request, 'vohni/team.html', {})

class JourneyDetailView(DetailView):
    model = Journey
    template_name = 'vohni/mandrivky.html'


class EmailCreateForm(ModelForm):
    class Meta:
        model = User_Email
        fields = ['name', 'email', 'journey_choice']

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
    #    self.helper.add_input(Submit('submit', u'Зберегти', css_class='btn btn-success'))
    #    self.helper.add_input(Submit('cancel_button', u'Скасувати', css_class='btn btn-danger'))

        # add buttons
        self.helper.layout.append(FormActions(
            Div(css_class = self.helper.label_class),
            Submit('add_button', u'Надіслати', css_class="btn btn-info"),
            HTML(u"<a class='btn btn-danger' name='cancel_button' href='{% url 'journeys' %}?status_message=Ви відмінили додавання своїх даних'>Скасувати</a>"),
        ))

#class for add group
class EmailCreateView(CreateView):
    model = User_Email
    template_name = 'vohni/user_email.html'
    form_class = EmailCreateForm
    

    def get_success_url(self):
        return u'%s?status_message=Дякуємо :) Ваші дані успішно надіслано. Чекайте на повідомлення від нас' % reverse('journeys')

    def post(self, request, *args, **kwargs):
        return super(EmailCreateView, self).post(request, *args, **kwargs)


