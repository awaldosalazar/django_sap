from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    no_personas = Persona.objects.count()
    return render(request, 'bienvenido.html', {'no_personas': no_personas})






#def despedirse(request):
#    return HttpResponse('Despedida desde Django')

#def contacto(request):
#    return HttpResponse({'"Email":"awaldosalazar@gmail.com","Tel":3318253863'})
