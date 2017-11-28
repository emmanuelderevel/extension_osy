from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Infos

# Create your views here.
def index(request):
    liste=Infos.objects.all()
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
