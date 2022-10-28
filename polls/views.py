from django.http import HttpResponse


def index(request):
    return HttpResponse("Django")

def inde(request):
    return HttpResponse('Fan')