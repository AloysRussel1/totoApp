from django.shortcuts import render, redirect, get_object_or_404
from .models import Toto

# Afficher la liste des Totos
def toto_list(request):
    totos = Toto.objects.all()
    return render(request, 'index.html', {'totos': totos})

# Ajouter un nouveau Toto
def add_toto(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_naissance = request.POST.get('date_naissance')
        photo = request.FILES.get('photo') if 'photo' in request.FILES else None

        # Créer et sauvegarder un nouvel objet Toto
        Toto.objects.create(
            nom=nom,
            prenom=prenom,
            date_naissance=date_naissance,
            photo=photo
        )
        return redirect('toto_list')

    return render(request, 'add_toto.html')

# Modifier un Toto
def edit_toto(request, toto_id):
    toto = get_object_or_404(Toto, pk=toto_id)
    if request.method == 'POST':
        # Mettre à jour les informations du Toto
        toto.nom = request.POST.get('nom')
        toto.prenom = request.POST.get('prenom')
        toto.date_naissance = request.POST.get('date_naissance')
        if 'photo' in request.FILES:
            toto.photo = request.FILES['photo']
        toto.save()
        return redirect('toto_list')

    # Afficher le formulaire pré-rempli pour modifier le Toto
    return render(request, 'add_toto.html', {'toto': toto})

# Supprimer un Toto
def delete_toto(request, toto_id):
    toto = get_object_or_404(Toto, pk=toto_id)
    if request.method == "POST":
        toto.delete()
        return redirect('toto_list')
    return render(request, 'delete_toto.html', {'toto': toto})
