from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index")
    #esto es una vista
#detalles de la encuesta
def detail(request, question_id):
    return HttpResponse("You're looking at question."% question_id)
#resultados de la encuesta
def results(request, question_id):
    response = "You're looking at the results of question%s"
    return HttpResponse(response % question_id)
#para contar las votaciones de la encuesta
def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)