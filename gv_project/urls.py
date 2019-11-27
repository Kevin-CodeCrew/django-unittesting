
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('good_vibes.urls')),
    path('admin/', admin.site.urls),
]
