from django.shortcuts import render
from app.models import Diagnostico
from app.models import Sintoma,Diagnostico
from django.contrib import messages
import clips
import os
from pathlib import Path

env = clips.Environment()

def paginaIndex(request):
    context = {}
    context['diagnostico'] = ''

    # Llenado de Diagnosticos
    diagnosticos = Diagnostico.objects.all()
    cont = 1
    for d in diagnosticos.all():
        print(d.simbolo)
        diagnostico1 = Diagnostico.objects.get(simbolo=d.simbolo)
        sintomas = ""
        for asd in diagnostico1.sintomas.all():
            sintomas += "(" + asd.simbolo + " S)"
        rule = "(defrule diagnostico" + str(cont) + " " + sintomas + " => (assert (diagnostico " + d.simbolo + ")))"
        env.build(rule)
        cont = cont + 1
    env.reset()
    # FIn llenado de Diagnosticos

    if request.method == 'POST':
        context['sintomas'] = Sintoma.objects.all()
        context['selected'] = ''
        return render(request, 'sintomas.html', context)
    else:
        return render(request, 'index.html')


def procesarView(request):
    context = {}
    context['diagnostico'] = ''
    ##Some code
    if request.method == 'POST':

        sint = request.POST.getlist('sintomas[]')
        print('Sintomas seleccionados: ', sint)
        for sin in sint:
            print('insertando sintoma: ',sin)
            env.assert_string("("+sin+" S)")
        env.run()
        context['diagnostico'] = 'No se ha encontrado un diagnóstico para los síntomas seleccionados'
        for fact in env.facts():
            if fact.template.name == 'diagnostico':
                print(fact[0])
                context['diagnostico'] = 'El diagnóstico es: ' + fact[0]


    context['selected'] = sint
    context['sintomas'] = Sintoma.objects.all()
    print('sintomas', context['sintomas'])
    print('diagnostico: ', context['diagnostico'])
    return render(request, 'sintomas.html', context)

def about(request):
    return render(request, 'about.html')