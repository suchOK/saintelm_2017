# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView, ListView
from django.forms import ModelForm
from .forms import EmailCreateForm


from .models import Journey, User_Email, CoverImage


# Create your views here.
def main_page(request):

    journeys = Journey.objects.filter(active=True).order_by('-start_date')[:2]
    cover_images = CoverImage.objects.all()

    return render(request, 'vohni/index.html', {'journeys': journeys, 'cover_images': cover_images})


class JourneyListView(ListView):
    model = Journey
    template_name = 'vohni/journey_list.html'


class JourneyDetailView(DetailView):
    model = Journey
    template_name = 'vohni/mandrivky.html'


#class for add group
class EmailCreateView(CreateView):
    model = User_Email
    template_name = 'vohni/user_email.html'
    form_class = EmailCreateForm
    

    def get_success_url(self):
        return u'%s?status_message=Дякуємо :) Ваші дані успішно надіслано. Чекайте на повідомлення від нас' % reverse('journeys')

    def post(self, request, *args, **kwargs):
        return super(EmailCreateView, self).post(request, *args, **kwargs)


