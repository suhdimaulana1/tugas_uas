from django.db import models

# Create your models here.
class Kelompok(models.Model):
    nama = models.CharField(max_length=30)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=244)
    penerbit = models.CharField(max_length=255)
    jumlah = models.IntegerField(null=True)
    kelompok_id = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.judul  

class Penulis(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tanggal_lahir = models.DateField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama  

class Peminjam(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    email = models.EmailField()
    nomor_telepon = models.CharField(max_length=15)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField()

    def __str__(self):
        return self.nama
