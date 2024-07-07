from django.contrib import admin
from django.urls import path, include
from perpustakaan.views import buku, penerbit, penulis, peminjam
from perpustakaan.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('kelompok', KelompokViewset)
router.register('Buku', BukuViewset)
router.register('Penulis', PenulisViewset)
router.register('Peminjam', PeminjamViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penerbit/', penerbit),
    path('penulis/', penulis),
    path('peminjam/', peminjam),
]