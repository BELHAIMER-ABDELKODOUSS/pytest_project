from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from documentation_app.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
