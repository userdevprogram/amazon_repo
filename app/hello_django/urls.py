from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload
from codehelp.views import index, codehelp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("upload/", image_upload, name="upload"),
    path("", index, name="index"),

    path("codehelp/", include('codehelp.urls'), name="codehelp"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
