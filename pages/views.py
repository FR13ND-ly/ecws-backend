from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Page
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import fitz
import os
from datetime import datetime

@csrf_exempt
def getPages(request):
    pages = []
    for page in Page.objects.all():
        pages.append("https://ecworks.pythonanywhere.com/media/pages/" + os.path.basename(page.file.name) + "?" + datetime.now().strftime("%d%m%Y%H%M%S"))
    return JsonResponse({"pages" : pages}, safe=False)


@csrf_exempt
def setPages(request):
    file = request.FILES['file']
    if os.path.exists(os.getcwd().replace("\\", "/") + "/media/main.pdf"):
        os.remove(os.getcwd().replace("\\", "/") + "/media/main.pdf")
    path = default_storage.save('main.pdf', ContentFile(file.read()))
    doc = fitz.open(os.path.join(settings.MEDIA_ROOT, path))
    for i in range(8):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        pix.save(settings.MEDIA_ROOT + '/pages/page' + str(i + 1) + ".png")
        newPage = Page.objects.get_or_create(id = i)[0]
        newPage.file = settings.MEDIA_ROOT + '/pages/page' + str(i + 1) + ".png"
        newPage.save()
    pages = []
    for page in Page.objects.all():
        pages.append("https://ecworks.pythonanywhere.com/media/pages/" + os.path.basename(page.file.name) + "?" + datetime.now().strftime("%d%m%Y%H%M%S"))
    return JsonResponse(pages, safe=False)



    