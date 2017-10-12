from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Essa é a view da balança!")

