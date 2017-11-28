from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Infos, Infos_string

# Create your views here.
def index(request):
    liste=Infos.objects.all()
    liste_string=Infos_string.objects.all()
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
