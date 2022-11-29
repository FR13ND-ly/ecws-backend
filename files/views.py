from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import File
import os

def formatDate(date):
    new_date = date.strftime("%d %B %Y, %H:%M").split()
    new_date[1] = new_date[1].capitalize()
    new_date = " ".join(new_date)
    return new_date

@csrf_exempt
def uploadFile(request):
    file = File.objects.create(file = request.FILES['file'])
    file.save()
    response = {
        "id" : file.id,
        "imageUrl" : "https://ecwrks.pythonanywhere.com/media/" + os.path.basename(file.file.name),
        "name" : file.file.name,
        "date" : formatDate(file.date)
    }
    return JsonResponse(response, safe=False)

@csrf_exempt
def removeFile(request, id):
    f = File.objects.get(id = id)
    if os.path.exists(os.getcwd().replace("\\", "/") + "/media/" + str(f.file)):
        os.remove(os.getcwd().replace("\\", "/") + "/media/" + str(f.file))
    f.delete()
    return JsonResponse({"status" : "succes"}, safe=False)