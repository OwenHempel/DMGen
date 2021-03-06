from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import *
from .forms import TownForm, NPCForm, ItemForm, ShopForm

import random

def randomizeTown(request):
    context = {}
    context['title'] = 'Randomly Generated Town'
    template_name = 'Towns/Randomize.html'
    nShops = int(random.gauss(4,1))
    nresidents = int(random.randrange(nShops,10))
    shops = []
    residents = []
    rforms = []
    sforms = []
    for i in range(nresidents):
        R = random.choice(Race.objects.all())
        A = random.choice(Age.objects.all())
        G = random.choice(Gender.objects.all().exclude(GenderText = 'Genderless'))
        FN = random.choice(Name.objects.all().filter(Race = R, Gender = G, Position = 1))
        try:
            LN = random.choice(Name.objects.all().filter(Race = R, Position = 2))
            N = NPC(Race = R, Age = A, Gender = G, LastName = LN, FirstName = FN)
        except:
            N = NPC(Race = R, Age = A, Gender = G, FirstName = FN)
        
        residents.append(N)
        rforms.append(NPCForm(instance = N))
    for i in range(nShops):
        T = random.choice(ShopType.objects.all())
        B = int(random.gauss(1000, 500))
        O = random.choice(residents)
        FN = random.choice(ShopName.objects.all().filter(Type = T, Position = 1))
        LN = random.choice(ShopName.objects.all().filter(Type = T, Position = 2))
        S = Shop(Type = T, Balance = B, FirstName = FN, LastName = LN, Owner = O)
        shops.append(S)
        sforms.append(ShopForm(instance = S))

    context['rForms'] = rforms
    context['sForms'] = sforms
    return render(request, template_name, context)



def Towndetail(request, town_id):
    context = {}
    context['title'] = 'Town Details'
    template_name = 'Towns/TownDetail.html'
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
    return render(request, template_name, context)

def TownList(request):
    template_name = 'Towns/TownList.html'
    context = {}
    context['MyTowns'] = Town.objects.all()
    context['title'] = 'List of Towns'
    return render(request, template_name, context)

def modifyNPC(request, npcid):
    context = {}
    context['npcid'] = npcid
    context['title'] = 'Modify World Info'
    template_name = 'Towns/ModifyNPC.html'
    instance = get_object_or_404(NPC, id=npcid)
    context['instance'] = instance
    if request.method == 'POST':
        form = NPCForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Towns:index', args = ('')))
    else:
        form = NPCForm(instance = instance)
    context['form'] = form
    return render(request, template_name, context) 
    
def modifyTown(request, tid):
    context = {}
    context['tid'] = tid
    context['title'] = 'Modify World Info'
    template_name = 'Towns/ModifyTown.html'
    instance = get_object_or_404(Shop, id=tid)
    context['instance'] = instance
    form = TownForm(instance = instance)
    if request.method == 'POST':
        form = TownForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Towns:index', args = ('')))
    context['form'] = form
    return render(request, template_name, context) 

def modifyShop(request, sid):
    context = {}
    context['sid'] = sid
    context['title'] = 'Modify World Info'
    template_name = 'Towns/ModifyShop.html'
    instance = get_object_or_404(Shop, id=sid)
    context['instance'] = instance
    form = ShopForm(instance = instance)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Towns:index', args = ('')))
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


