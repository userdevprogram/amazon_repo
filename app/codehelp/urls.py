
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from codehelp.views import index, codehelp, group

urlpatterns = [
    path("", codehelp, name="codehelp"),
    path("<int:group_id>/", codehelp, name="codehelp"),
]

