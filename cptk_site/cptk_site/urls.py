from django.contrib import admin
from django.urls import path, include

from apps.main import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', include('account.urls'), name='account'),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls'), name='catalog'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()