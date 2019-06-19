from django.http import HttpResponse

# Create your views here - tomek michalik june
def index(request):
    return HttpResponse("Hello, world. you're at the polls index.")
