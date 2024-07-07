from django.shortcuts import render


def buku(request):
    judul = "Belajar Membaca"
    penulis = "Sohebul Bahri"

    konteks = {
        'title': judul,
        'penulis': penulis,
    }
    return render(request, 'buku.html', konteks)



def penerbit(request):
     return render(request, 'penerbit.html')

def penulis(request):
    return render(request, 'penulis.html')    

def peminjam(request):
    return render(request, 'peminjam.html')     
