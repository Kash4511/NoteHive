from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('myapp/', include('myapp.urls')),
    path('', views.index , name = 'index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registration_view , name = 'register'),

    path("__reload__/", include("django_browser_reload.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



