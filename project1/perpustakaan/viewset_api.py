from perpustakaan.models import Kelompok, Buku, Penulis, Peminjam
from perpustakaan.serializers import KelompokSerializers, BukuSerializers, PenulisSerializers, PeminjamSerializers
from rest_framework import viewsets, permissions

class KelompokViewset(viewsets.ModelViewSet):
    queryset = Kelompok.objects.all()
    serializer_class = KelompokSerializers
    permission_classes = [permissions.IsAuthenticated]
class BukuViewset(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializers
    permission_classes = [permissions.IsAuthenticated]
class PenulisViewset(viewsets.ModelViewSet):
    queryset = Penulis.objects.all()
    serializer_class = PenulisSerializers 
    permission_classes = [permissions.IsAuthenticated]
class PeminjamViewset(viewsets.ModelViewSet):
    queryset = Peminjam.objects.all()
    serializer_class = PeminjamSerializers 
    permission_classes = [permissions.IsAuthenticated]