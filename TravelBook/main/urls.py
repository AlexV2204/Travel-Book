from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)