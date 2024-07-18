from django.shortcuts import render,redirect, get_object_or_404
from dashboard.forms import BarangForm,UserForm
from dashboard.models import Barang, User
from django.contrib import messages

# Create your views here.
def home_redirect(request):
    return redirect('home')

def home(request):
    pagetitle = "Home"
    konteks = {
        'title': pagetitle,
    }
    return render(request, "home.html", konteks)

def produkl(request):
    pagetitle = "Laki-Laki"
    konteks = {
        'title': pagetitle,
    }
    return render(request, "produk-laki-laki.html", konteks)

def produkp(request):
    pagetitle = "Perempuan"
    konteks = {
        'title': pagetitle,
    }
    return render(request, "produk-perempuan.html", konteks)
def seluruhproduk(request):
    pagetitle = "Seluruh Produk"
    konteks = {
        'title': pagetitle,
    }
    return render(request, "seluruh-produk.html", konteks)
def contact(request):
    pagetitle = "Contact Person"
    konteks = {
        'title': pagetitle,
    }
    return render(request, "contact-person.html", konteks)

def Barang_View(request):
    barangs = Barang.objects.all()
    return render(request, 'tampil_brg.html', {'barangs': barangs})

def tambah_barang(request):
    if request.method == 'POST':
        form = BarangForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = BarangForm()
    else:
        form = BarangForm()
    
    konteks = {
        'form': form,
    }
    return render(request, 'tambah_barang.html', konteks)



def ubah_brg(request, id_barang):
    barangs = Barang.objects.get(id=id_barang)
    if request.method == 'POST':
        form = BarangForm(request.POST, request.FILES, instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Barang berhasil diubah.")
            form = BarangForm()

    else:
        form = BarangForm(instance=barangs)
    
    konteks = {
        'form': form,
    }
    return render(request, 'ubah_brg.html', konteks)

def hapus_brg(request, id_barang):
    print("id.barang")
    barang = Barang.objects.filter(id=id_barang)
    barang.delete()
    messages.success(request, 'Barang berhasil dihapus!')
    return redirect('Vbrg')

def User_View(request):
    users = User.objects.all()
    konteks = {
        'users': users,
    }
    return render(request, 'tampil_user.html', konteks)

def tambah_user(request):
    konteks = {}  # Inisialisasi konteks di luar blok if-else
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = UserForm()  # Inisialisasi form baru setelah berhasil menyimpan
    else:
        form = UserForm()

    konteks['form'] = form  # Memasukkan form ke dalam konteks

    return render(request, 'tambah_user.html', konteks)

def ubah_user(request, id_user):
    users = User.objects.get(id=id_user)
    if request.POST:
        form=UserForm(request.POST,instance=users)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_user', id_user=id_user)
    else:
        form=UserForm(instance=users)
        konteks = {
            'form':form,
            'users' :users
        }
    return render(request, 'ubah_user.html',konteks )

def hapus_user(request, id_user):
    users= User.objects.filter(id=id_user)
    users.delete()
    messages.success(request,"Data Terhapus")
    return redirect('user')

