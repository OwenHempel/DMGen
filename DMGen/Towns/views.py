from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Town, Shop, NPC
from .forms import TownForm

def TownList(request):
    template_name = 'Towns/TownList.html'
    context = {}
    form = TownForm()
    context['form'] = form
    context['MyTowns'] = Town.objects.all()
    return render(request, template_name, context)

def Generate(request):
	context = {}
	template_name = 'Generate.html'
	if request.method == 'POST':
		pass
	else:	
		form = TownForm()
    context['form'] = form
    return render(request, template_name, context)

def Towndetail(request, town_id):
	sTown = get_object_or_404(Town, pk=town_id)
	return render(request, 'Towns/TownDetail.html', {'Town': sTown})


