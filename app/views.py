from django.shortcuts import render
from app.models import diagnostico
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
    return render(request, 'index.html')


def procesarView(request):
    ##Some code
    return render(request, 'result.html')
