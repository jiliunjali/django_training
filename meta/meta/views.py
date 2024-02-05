#file is created to do error handling for project
from django.http import HttpResponse,HttpResponseNotFound

def handler404(request, exception):
    print("handler is being called")
    return HttpResponse("404 : PAGE NOT FOUND") # for wanting our own page to display just make html fileor page that to be displayed here. 

def home(request):
    return HttpResponseNotFound("LittleLemon")