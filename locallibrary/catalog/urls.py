# Используйте include() чтобы добавлять URL из каталога приложения
from django.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
     path('catalog/', include('catalog.urls')),
]