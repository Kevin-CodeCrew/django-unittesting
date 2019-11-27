from django.http import HttpResponse
from django.shortcuts import render
from django.utils.crypto import random

good_vibes_msg = [
    "Everything you need is within you.",
    "Inhale confidence, exhale doubt."
]


# Home Page
def index(req):
    return HttpResponse("The Good Vibes Page!!!")


# Message of the day
def mod(req):
    rannum = random.randrange(0, 2)
    context = {'mod': good_vibes_msg[rannum]}
    return render(req, 'good_vibes/mod.html', context)
