import django.shortcuts

from django.http import HttpResponse, response

# Create your views here.

def detail(request, question_id):
    return HttpResponse("ciao tutti sei nella pagina di index polls %s. " % question_id)

def results(request, question_id):
    response = "stai guardano il resultato di domanda %s."
    return HttpResponse(response, question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s. "% question_id)
    
            

