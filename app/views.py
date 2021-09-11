from django.shortcuts import render
from app.models import Diagnostico
from app.models import Sintoma
from django.contrib import messages
import clips
import os
from pathlib import Path


def paginaIndex(request):
    env = clips.Environment()

    rule = """
    (defrule my-rule
      (my-fact first-slot)
      =>
      (printout t "My Rule fired!" crlf))
    """
    # env.build("reglas.clp")
    env.load("reglas.clp")
    for rule in env.rules():
        print(rule)

    return procesarView(request)


def procesarView(request):
    ##Some code
    if request.method == 'POST':
        sint = request.POST.getlist('sintomas[]')
        print(sint)
        sintomas = Sintoma.objects.all()
        print(sintomas)
        return render(request, 'sintomas.html', {"sintomas": sintomas})
    else:
        sintomas = Sintoma.objects.all()
        print(sintomas)
        return render(request, 'sintomas.html', {"sintomas": sintomas})
