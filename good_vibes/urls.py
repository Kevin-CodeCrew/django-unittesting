from django.urls import path
from . import views
urlpatterns = [
    path('mod/', views.mod, name='mod'),
    path('', views.index, name='index')
]