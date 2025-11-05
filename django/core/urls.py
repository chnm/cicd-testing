import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import index as core_index
from cicd_testing.views import index as cicd_testing_index
from upload.views import upload_page

urlpatterns = [
    path('', core_index, name='index'),
    path('cicd_testing/', cicd_testing_index, name='cicd_testing'),
    path('upload/', upload_page, name='upload'),

    path('admin/', admin.site.urls),

    # allauth
    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
