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
    context['MyTowns'] = Town.objects.all()
    context['title'] = 'List of Towns'
    return render(request, template_name, context)

def modify(request):
    context = {}
    context['title'] = 'Modify World Info'
    template_name = 'Towns/Modify.html'
    if request.method == 'POST':
        if 'NPC' in request.POST:
            npcid = request.POST['NPC']
            instance = get_object_or_404(NPC, id=npcid)
            form = NPCForm(instance = instance)
        elif 'Shop' in request.POST:
            sid = request.POST['Shop']
            instance = get_object_or_404(Shop, id=sid)
            form = ShopForm(instance = instance)
        elif 'Town' in request.POST:
            tid = request.POST['Town']
            instance = get_object_or_404(Town, id=tid)
            form = TownForm(instance = instance)
    context['form'] = form
    return render(request, template_name, context)       
    
def Generate(request):
    context = {}
    template_name = 'Towns/Generate.html'
    if request.method == 'POST':
        form1 = TownForm(request.POST)
        form2 = NPCForm(request.POST)
        form3 = ShopForm(request.POST)
        form4 = ItemForm(request.POST)
        if form1.is_valid():
            T = Town(Name = form1.cleaned_data['Name'])
            T.save()
            T.Shops.set(form1.cleaned_data['Shops'])
            T.Residents.set(form1.cleaned_data['Residents'])
            T.save()
        if form2.is_valid():
            C = NPC(FirstName = form2.cleaned_data['FirstName'], LastName = form2.cleaned_data['LastName'], Race = form2.cleaned_data['Race'], Age = form2.cleaned_data['Age'], Gender = form2.cleaned_data['Gender'])
            C.save()
            C.Appearance.set(form2.cleaned_data['Appearance'])
            C.Personality.set(form2.cleaned_data['Personality'])
            C.save()
        if form3.is_valid():
            S = Shop(FirstName = form3.cleaned_data['FirstName'], LastName = form3.cleaned_data['LastName'], Owner = form3.cleaned_data['Owner'], Balance = form3.cleaned_data['Balance'], Type = form3.cleaned_data['Type'])
            S.save()
            S.Inventory.set(form3.cleaned_data['Inventory'])
            S.save()
        if form4.is_valid():
            I = Item(Name = form4.cleaned_data['Name'], Cost = form4.cleaned_data['Cost'], Type = form4.cleaned_data['Type'])
            I.save()
            I.Effect.set(form4.cleaned_data['Effect'])
            I.save()
        return HttpResponseRedirect(reverse('Towns:Generate', args = ('')))
    else:   
        form1 = TownForm()
        form2 = NPCForm()
        form3 = ShopForm()
        form4 = ItemForm()
        context['form1'] = form1
        context['form2'] = form2
        context['form3'] = form3
        context['form4'] = form4
    context['title'] = 'Generate World Info'

    return render(request, template_name, context)

def Towndetail(request, town_id):
    context = {}
    context['title'] = 'Town Details'
    sTown = get_object_or_404(Town, pk=town_id)
    if request.method == 'POST':
        iDict = request.POST.dict()
        iDict.pop('csrfmiddlewaretoken')
        for i in iDict:
            shop = Shop.objects.get(id = int(iDict[i]))
            item = Item.objects.get(id = int(i))
            shop.Inventory.remove(item)
            shop.Balance += item.Cost
            shop.save()

    context['Town'] = sTown
    return render(request, 'Towns/TownDetail.html', context)


