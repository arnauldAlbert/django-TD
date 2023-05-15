from django.urls import path

from . import views

urlpatterns = [
    path('ajout/',views.ajout),
    path('traitement/',views.traitement),
    path('index/',views.index),
    path('affiche/<int:id>/', views.affiche),
]