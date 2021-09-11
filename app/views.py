from django.shortcuts import render
from app.models import Diagnostico
from app.models import Sintoma,Diagnostico
from django.contrib import messages
import clips
import os
from pathlib import Path


def paginaIndex(request):
    context = {}
    context['diagnostico'] = ''

    rule = """
    (defrule my-rule
      (my-fact first-slot)
      =>
      (printout t "My Rule fired!" crlf))
    """
    # env.build("reglas.clp")
    #for rule in env.rules():
    #    print(rule)
    diagnostico1 = Diagnostico.objects.get(resultado='Diagnóstico prueba')
    for asd in diagnostico1.sintomas.all():
        print(asd.simbolo)
    return render(request, 'sintomas.html', context)
    return procesarView(request)


def procesarView(request):
    context = {}
    context['diagnostico'] = ''
    ##Some code
    if request.method == 'POST':
        env = clips.Environment()
        env.load("reglas.clp")
        env.reset()
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
    context['sintomas'] = Sintoma.objects.all()
    print('sintomas', context['sintomas'])
    print('diagnostico: ', context['diagnostico'])
    return render(request, 'sintomas.html', context)
