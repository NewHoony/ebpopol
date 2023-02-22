from django.shortcuts import render


def index(req):
    return render(req,"coverletter/index.html")

# Create your views here.
