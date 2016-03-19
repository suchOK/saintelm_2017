from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Journey


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
