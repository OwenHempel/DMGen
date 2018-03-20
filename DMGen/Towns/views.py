from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Town, Shop, NPC, Item
from .forms import TownForm, NPCForm, ItemForm, ShopForm

def TownList(request):
    template_name = 'Towns/TownList.html'
    context = {}
    form = TownForm()
    context['form'] = form
    context['MyTowns'] = Town.objects.all()
    return render(request, template_name, context)

def Generate(request):
    context = {}
    template_name = 'Towns/Generate.html'
    if request.method == 'POST':
        form1 = TownForm()
        form2 = NPCForm()
        form3 = ShopForm()
        form4 = ItemForm()
        if form1.is_valid():
            T = Town(Name = form1.Name, Shops = form1.Shops, Residents = form1.Residents)
        if form2.is_valid():
            C = NPC(FirstName = form2.FirstName, LastName = form2.LastName, Race = Form2.Race, Age = form2.Age, Gender = form2.Gender,
            Appearance = form2.Appearance, Personality = form2.Personality)
            C.save()
        return HttpResponseRedirect(reverse('Towns:Generate', args=()))
    else:   
        form1 = TownForm()
        form2 = NPCForm()
        form3 = ShopForm()
        form4 = ItemForm()
        context['form1'] = form1
        context['form2'] = form2
        context['form3'] = form3
        context['form4'] = form4

    return render(request, template_name, context)

def Towndetail(request, town_id):
    sTown = get_object_or_404(Town, pk=town_id)
    return render(request, 'Towns/TownDetail.html', {'Town': sTown})


