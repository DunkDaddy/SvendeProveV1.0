from django.urls import path
from .views import *

urlpatterns = [
    path('BrugerListe/', bruger_liste),
    path('KategoriListe/', kategori_liste),
    path('GeoListe/', geo_liste),
    path('SubscribedListe/', subscribed_liste),
    path('BillederListe/', billeder_liste),

    path('BrugerCreate/', bruger_create),
    path('KategoriCreate/', kategori_create),
    path('GeoCreate/', geo_create),
    path('SubscribedCreate/', subscribed_create),
    path('BillederCreate/', billeder_create),

    path('Bruger/<int:pk>/', bruger_view),
    path('Kategori/<int:pk>/', kategori_view),
    path('Geo/<int:pk>/', geo_view),
    path('Subscribed/<int:pk>/', subscribed_view),
    path('Billeder/<int:pk>/', billeder_view),

    path('BrugerUpdate/', bruger_update),
    path('KategoriUpdate/', kategori_update),
    path('GeoUpdate/', geo_update),
    path('SubscribedUpdate/', subscribed_update),
    path('BillederUpdate/', billeder_update),

    path('BrugerDelete/', bruger_delete),
    path('KategoriDelete/', kategori_delete),
    path('GeoDelete/', geo_delete),
    path('SubscribedDelete/', subscribed_delete),
    path('BillederDelete/', billeder_update),


    path('PC/', password_check),
    path('BC/', brugernavn_check),
]