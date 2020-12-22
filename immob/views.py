from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, BesoinForm
import json


def index(request):

    if loggedUser(request):
        return render(request, 'immob/index.html', { 'user' : request.user, 'log': loggedUser(request), 'userForm': UserCreationForm})

    return render(request, 'immob/index.html', { 'userForm': UserCreationForm })


def register(request):
    
    if len(request.POST) > 0:

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'message': "Success"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'message': "Incomplete"}), content_type="application/json")

    return HttpResponse(json.dumps({'message': "No data"}), content_type="application/json")



def bien(request):

    if loggedUser(request):
        return render(request, 'immob/public/bien.html', { 'user': request.user, 'log': loggedUser(request)})
    
    return render(request, 'immob/public/bien.html', {'userForm': UserCreationForm})

def contacter_agence(request):

    if loggedUser(request):
        return render(request, 'immob/public/contacter_agence.html', { 'user': request.user, 'log': loggedUser(request)})

    return render(request, 'immob/public/contacter_agence.html', {'userForm': UserCreationForm})


def poster(request):

    besoinForm = BesoinForm()

    if len(request.POST) > 0:

        besoinForm = BesoinForm(request.POST)
        if loggedUser(request)
            besoinForm.user = request.user

            if besoinForm.is_valid():
                besoinForm.save()
                




def Login(request):

    #Authentification
    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(email=email, password=password) #Recupere l'utilisateur 

    if user is not None:
        if user.is_active:
            request.session['id'] = user.username #Ajout à la variable de session
            login(request, user) #Connexion
            return HttpResponse(json.dumps({'message': "Success"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'message': "inactive"}), content_type="application/json")
    else:

        return HttpResponse(json.dumps({'message': "invalid"}), content_type="application/json") #Echec
    return HttpResponse(json.dumps({'message': "denied"}), content_type="application/json")
    

def Logout(request):

    #Deconnexion d'un utilisateur
    if loggedUser(request):
        del request.session['id']
        logout(request)
        return redirect('immob:index')
    else: #Si aucun utilisateur n'est connecté
        return None 

def loggedUser(request):

    #Voir si un utilisateur est connecté
    if 'id' in request.session:
        return True
    else:
        return False #Aucun utilisateur n'est connecté