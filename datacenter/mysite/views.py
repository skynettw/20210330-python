from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	myname = "何敏煌"
	return render(request, 'index.html', locals())
