from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse("Here's the text of the Web page.")
    return render(request, 'blog/index.html', locals())

