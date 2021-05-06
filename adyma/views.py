from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Beneficiaire, Etablissement, Groupe, Activite, Test, Psychosocial, Structurel, Physique, Presence
from .forms import BeneficiaireForm , EtablissementForm, GroupeForm, GroupeChangeListForm, ActiviteForm, TestForm, PsychosocialForm, PresenceForm, PhysiqueForm, StructurelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .filters import BeneficiaireFilter

# Create your views here.
@login_required
def coach(request):
    return render(request, 'adyma/coach.html')





#_______________________________views_home_page_________________
@login_required
def home(request):
    items = Beneficiaire.objects.all()
    if request.method == 'POST':
        form =  BeneficiaireForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BeneficiaireForm()
    context = {
        'items':items,
        'form':form,
    }
    return render(request, 'adyma/home.html', context)

#____________filtre




#_________recherche

@login_required
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        patients = Beneficiaire.objects.filter(nom__iexact=searched)
        prenoms = Beneficiaire.objects.filter(prenom__iexact=searched)
        etablis = Etablissement.objects.filter(nom_etablissement__contains=searched)
        return render(request,'partials/search.html',{'searched':searched,
        'patients':patients, 'prenoms':prenoms, 'etablis':etablis})

    else:
        return render(request,'partials/search.html', {})


def filtre(request):
    beneficiaire_list = Beneficiaire.objects.all()
    beneficiaire_filter = BeneficiaireFilter(request.GET, queryset=beneficiaire_list)
    return render(request, 'beneficiaire.html', {'filter':beneficiaire_filter})

#___________________________________Beneficiaires_views_______________________

@login_required
def entretien(request):
    if request.method == 'POST':
        form = BeneficiaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficiaire')
    else:
        form = BeneficiaireForm()
    return render(request, 'formulaires/inscription.html', {'form': form})


@login_required
def beneficiaire_vue(request):
    items = Beneficiaire.objects.all()
    #items = Beneficiaire.objects.raw('SELECT * FROM adyma_beneficiaire order by nom')
   
    context={
        'items':items,
        
    }
    return render(request, 'vues/beneficiaire.html',context)

@login_required
def beneficiaire_delete(request, pk):
    item = Beneficiaire.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('beneficiaire')
    return render(request, 'modif/beneficiaire_delete.html')

@login_required
def beneficiaire_update(request, pk):
    item = Beneficiaire.objects.get(id=pk)
    if request.method == 'POST':
        form = BeneficiaireForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('beneficiaire')
    else:
        form = BeneficiaireForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'modif/beneficiaire_update.html', context)


@login_required
def beneficiaire_detail(request,pk):
    beneficiaires = Beneficiaire.objects.get(id=pk)
    context = {
        'beneficiaires': beneficiaires,
    }
    return render(request, "vues/beneficiaire_detail.html", context)


#_________________________________________groupe

@login_required
def groupe(request):
    if request.method == 'POST':
        form = GroupeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GroupeForm
    return render(request, 'formulaires/groupe.html', {'form':form})


@login_required
def groupe_vue(request):
    equipes = Groupe.objects.all()
    context = {
        'equipes':equipes
    }
    return render(request, 'vues/groupe_vue.html', context)

@login_required
def groupe_delete(request, pk):
    equipes = Groupe.objects.get(id=pk)
    if request.method == 'POST':
        equipes.delete()
        return redirect('groupe_vue')
    return render(request, 'modif/groupe_delete.html')

@login_required
def groupe_update(request, pk):
    equipe = Groupe.objects.get(id=pk)
    if request.method == 'POST':
        form = GroupetForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('beneficiaire')
    else:
        form = GroupeForm(instance=equipe)
    context = {
        'form': form,
    }
    return render(request, 'modif/groupe_update.html', context)



#________________________test

@login_required
def test(request):
    if request.method =='POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TestForm()
    return render(request, 'formulaires/test.html', {'form':form})


@login_required
def test_delete(request, pk):
    teste = Test.objects.get(id=pk)
    if request.method == 'POST':
        teste.delete()
        return redirect('beneficiaire')
    return render(request, 'modif/test_delete.html')

@login_required
def test_update(request, pk):
    teste = Test.objects.get(id=pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=teste)
        if form.is_valid():
            form.save()
            return redirect('beneficiaire')
    else:
        form = TestForm(instance=teste)
    context = {
        'form': form,
    }
    return render(request, 'modif/test_update.html', context)

@login_required
def test_detail(request,id):
    testes = Test.objects.filter(beneficiaire_id = id)
    context = {
        'testes': testes,
        
    }
    return render(request, "vues/test_detail.html", context)
#________________________________etablissement___________-


@login_required
def etablissement(request): #__enregistrement d'etablissement
    if request.method == 'POST':
        form = EtablissementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etablissement_vue')
    else:
        form = EtablissementForm()
    return render(request, 'formulaires/etablissement.html', {'form':form})

@login_required
def etablissement_vue(request):
    residences = Etablissement.objects.all()
    #items = Etablissement.objects.raw('SELECT * FROM adyma_etablissement')
    context={
        'residences':residences,
        
    }
    return render(request, 'vues/etablissement_vue.html',context)

@login_required
def etablissement_delete(request, pk):
    residence = Etablissement.objects.get(id=pk)
    if request.method == 'POST':
        residence.delete()
        return redirect('etablissement_vue')
    return render(request, 'modif/etablissement_delete.html')


@login_required
def etablissement_update(request, pk):
    residence = Etablissement.objects.get(id=pk)
    if request.method == 'POST':
        form = EtablissementForm(request.POST, instance=residence)
        if form.is_valid():
            form.save()
            return redirect('beneficiaire')
    else:
        form = EtablissementForm(instance=residence)
    context = {
        'form': form,
    }
    return render(request, 'modif/etablissement_update.html', context)

@login_required
def etablissement_detail(request,pk):
    etablissements = Etablissement.objects.get(id=pk)
    groups = Etablissement.objects.filter(id=pk)
    context = {
        'etablissements': etablissements,
        'groups':groups
    }
    return render(request, "vues/etablissement_detail.html", context)



#___________psychosocial

@login_required
def psychosocial(request):
    if request.method == 'POST':
        form = PsychosocialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficiaire')
    else:
        form = PsychosocialForm()
    return render(request, 'formulaires/psychosocial.html', {'form': form})


@login_required
def psychosocial_vue(request):
    psycho = Psychosocial.objects.all()
    context = {
        'psycho' : psycho
    }
    return render(request. vues/psychosocial_vue.html)

@login_required
def psychosocial_delete(request, pk):
    psycho = Psychosocial.objects.all(id=pk)
    print(psycho)
    if request.method == 'POST':
        psycho.delete()
        return redirect('beneficiaire')
    return render(request, 'modif/psychosocial_delete.html')


@login_required
def psychosocial_detail(request,id):
    psychos = Psychosocial.objects.filter(beneficiaire_id = id)
    context = {
        'psychos': psychos,
    }
    return render(request, "vues/psychosocial_detail.html", context)

#__________Presence


@login_required
def presence(request):
    if request.method == 'POST':
        form = PresenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presence_detail')
    else:
        form = PresenceForm()
    return render(request, 'formulaires/presence.html', {'form': form})

def presence_update(request):
    present = Presence.objects.get(id=pk)
    if request.method == 'POST':
        form = PresenceForm(request.POST, instance=present)
        if form.is_valid():
            form.save()
            return redirect('presence_vue')
    else:
        form = PresencetForm(instance=present)
    context = {
        'form': form,
    }
    return render(request, 'modif/presence_update.html', context)

#___________Activite


@login_required
def activite(request):
    if request.method == 'POST':
        form = Activite(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficiaire')
    else:
        form = ActiviteForm()
    return render(request, 'formulaires/activite.html', {'form': form})

def activite_update(request):
    activ = Activite.objects.get(id=pk)
    if request.method == 'POST':
        form = ActiviteForm(request.POST, instance=activ)
        if form.is_valid():
            form.save()
            return redirect('presence_vue')
    else:
        form = PresencetForm(instance=activ)
    context = {
        'form': form,
    }
    return render(request, 'modif/activite_update.html', context)

#__________________Physique
@login_required
def physique(request):
    if request.method == 'POST':
        form = PhysiqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficiaire')
    else:
        form = PhysiqueForm()
    return render(request, 'formulaires/physique.html', {'form': form})

@login_required
def physique_delete(request, pk):
    forme = Physique.objects.get(id=pk)
    if request.method == 'POST':
        forme.delete()
        return redirect('beneficiaire')
    return render(request, 'modif/physique_delete.html')
    
def physique_update(request):
    formes = Physique.objects.get(id=pk)
    if request.method == 'POST':
        form = PhysiqueForm(request.POST, instance=forme)
        if form.is_valid():
            form.save()
            return redirect('presence_vue')
    else:
        form = PhysiqueForm(instance=forme)
    context = {
        'formes': formes,
    }
    return render(request, 'modif/physique_update.html', context)

def physique_detail(request,id):
    formes = Physique.objects.filter(beneficiaire_id = id)
    context = {
        'formes': formes
    }
    return render(request, "vues/physique_detail.html", context)

#_____________structurel

@login_required
def structurel(request):
    if request.method == 'POST':
        form = Structurel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beneficiaire')
    else:
        form = StructurelForm()
    return render(request, 'formulaires/structurel.html', {'form': form})

@login_required
def structurel_delete(request, pk):
    structure = Structurel.objects.get(id=pk)
    if request.method == 'POST':
        structuree.delete()
        return redirect('etablissement_vue')
    return render(request, 'modif/structurel_delete.html') 


@login_required
def structurel_update(request):
    structure = Structurel.objects.get(id=pk)
    if request.method == 'POST':
        form = StructurelForm(request.POST, instance=structure)
        if form.is_valid():
            form.save()
            return redirect('etablissement_vue')
    else:
        form = PhysiqueForm(instance=structure)
    context = {
        'form': form,
    }
    return render(request, 'modif/structurel_update.html', context)