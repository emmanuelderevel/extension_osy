from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Infos, Infos_string

from .forms import ConnexionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Create your views here.
@login_required()
def index(request):
    liste=list(Infos.objects.all())
    liste_string=list(Infos_string.objects.all())
    return render(request, 'blog/index.html', locals())

def test(request):
    if request.method == 'POST':
          queryDict=request.POST
          myDict = dict(queryDict)
          username=myDict['username'][0]
          password=myDict['password'][0]
          url=myDict['url'][0]
          a=Infos(username=username, password=password, url=url)
          a.save()
          #print('Post : {}'.format(request.POST))
          #print('Body : {}'.format(request.body))
          #print('Data : {}'.format(myDict))
          return HttpResponse('')

def test_string(request):
    if request.method == 'POST':
          queryDict=request.POST
          myDict = dict(queryDict)
          infos=myDict['infos'][0]
          a=Infos_string(infos=infos)
          a.save()
          #print('Post : {}'.format(request.POST))
          #print('Body : {}'.format(request.body))
          #print(infos)
          return HttpResponse('')

def test_new(request):
    if request.method == 'POST':
          queryDict=request.POST
          myDict = dict(queryDict)
          print('Post : {}'.format(request.POST))
          print('Body : {}'.format(request.body))
          print(myDict)
          a=0
          for cle in myDict:
              a=cle
          print(a)
          b=Infos_string(infos=a)
          b.save()
          print(Infos_string.objects.all())
          return HttpResponse('')

def connexion(request):
    error = False
    next = request.GET.get('next')
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)
                next = request.POST.get('next')
                return HttpResponseRedirect(next)
            else: # sinon une erreur sera affichée
                error = True
                next = request.POST.get('next')
    else:
        form = ConnexionForm()
    return render(request, 'blog/connexion.html', locals())

def sign_out(request):
    logout(request)
    return redirect('index')
