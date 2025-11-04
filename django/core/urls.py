import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from cicd_testing.views import index
from upload.views import image_upload

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('upload/', image_upload, name='upload'),

    # allauth
    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
