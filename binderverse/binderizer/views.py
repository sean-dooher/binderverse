from django.http import HttpResponse
from django.shortcuts import render


def binderize(request):
    return HttpResponse("=)")
