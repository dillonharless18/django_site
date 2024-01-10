from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def super_cool_poll(request):
    return HttpResponse("Hello, world. You're at the super_cool_poll index.")