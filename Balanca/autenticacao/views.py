from django.http import HttpResponse

def index(request):
    return HttpResponse("Essa é a view de autenticao!!!")