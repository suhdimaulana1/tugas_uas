from perpustakaan.models import Kelompok, Buku, Penulis, Peminjam
from rest_framework import serializers

class KelompokSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kelompok
        fields = ['id', 'nama', 'keterangan']
class BukuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ['judul', 'penulis', 'penerbit', 'jumlah', 'kelompok_id', 'tanggal']
class PenulisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Penulis               
        fields = ['nama', 'email', 'tanggal_lahir', 'deskripsi' ]
class PeminjamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Peminjam
        fields = ['nama', 'alamat', 'email', 'nomor_telepon', 'buku', 'tanggal_pinjam', 'tanggal_kembali' ]