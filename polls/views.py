import django.shortcuts

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("ciao tutti sei nella pagina di index polls.")
