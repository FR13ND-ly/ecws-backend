from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('files/', include('files.urls')),
    re_path(r'^api/media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]