from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('home', include('home.urls')),
    path('switch/', include('switch.urls')),
    path('Computador/', include('Computador.urls')),
]